import os

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


BASE_URL = os.environ.get("QA_BASE_URL", "http://localhost:8092/")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


TEXT_TARGETS = {
    ".hotspot--dogs": (54, 78),
    ".hotspot--partners": (74, 104),
    ".hotspot--market": (58, 82),
    ".hotspot--shelter": (78, 108),
    ".hotspot--faq": (70, 100),
    ".hotspot--contacts": (78, 108),
    ".hotspot--menu-dogs": (360, 450),
    ".hotspot--menu-activities": (620, 760),
    ".hotspot--menu-market": (260, 340),
    ".hotspot--menu-shelter": (310, 410),
    ".hotspot--menu-djs": (120, 180),
    ".hotspot--menu-faq": (245, 325),
    ".hotspot--contact-1": (205, 225),
    ".hotspot--contact-2": (150, 170),
    ".hotspot--contact-3": (190, 210),
    ".hotspot--contact-4": (260, 280),
}


CONTROL_TARGETS = {
    ".hotspot--klepa": (245, 280, 375, 420),
    ".hotspot--belka": (245, 280, 375, 420),
    ".hotspot--tolik": (245, 280, 375, 420),
    ".hotspot--persey": (245, 280, 375, 420),
    ".hotspot--cards-prev": (50, 80, 90, 125),
    ".hotspot--cards-next": (50, 80, 90, 125),
    ".hotspot--activity-1": (380, 420, 190, 215),
    ".hotspot--activity-2": (380, 420, 190, 215),
    ".hotspot--activity-3": (380, 420, 190, 215),
    ".hotspot--activity-4": (380, 420, 190, 215),
    ".hotspot--activity-5": (380, 420, 190, 215),
    ".hotspot--activity-6": (380, 420, 190, 215),
    ".hotspot--partners-row": (1180, 1260, 110, 135),
    ".hotspot--market-logos": (920, 955, 300, 330),
    ".hotspot--shelter-site": (240, 300, 40, 70),
    ".hotspot--faq-1": (780, 835, 30, 48),
    ".hotspot--faq-2": (780, 835, 30, 48),
    ".hotspot--faq-3": (780, 835, 30, 48),
    ".hotspot--faq-4": (780, 835, 30, 48),
    ".hotspot--faq-5": (780, 835, 30, 48),
    ".hotspot--faq-6": (780, 835, 30, 48),
}


POSITION_TARGETS = {
    ".hotspot--activity-1": (80, 95, 3650, 3670),
    ".hotspot--activity-2": (515, 530, 3650, 3670),
    ".hotspot--activity-3": (950, 965, 3650, 3670),
    ".hotspot--activity-4": (80, 95, 3870, 3890),
    ".hotspot--activity-5": (515, 530, 3870, 3890),
    ".hotspot--activity-6": (950, 965, 3870, 3890),
    ".hotspot--partners-row": (110, 120, 4145, 4165),
    ".hotspot--market-logos": (250, 260, 4695, 4710),
    ".hotspot--shelter-site": (575, 585, 5695, 5705),
}


ALL_HOTSPOTS = [
    *TEXT_TARGETS.keys(),
    *CONTROL_TARGETS.keys(),
]


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        launch_options = {}
        if os.path.exists(CHROME_PATH):
            launch_options["executable_path"] = CHROME_PATH
        browser = playwright.chromium.launch(**launch_options)
        yield browser
        browser.close()


def new_page(browser, width=1440, height=1000):
    page = browser.new_page(viewport={"width": width, "height": height})
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.goto(BASE_URL, wait_until="networkidle")
    page.wait_for_selector(".festival-page__image")
    return page, errors


def artboard_rect(page):
    return page.locator(".festival-page__artboard").evaluate(
        "el => { const r = el.getBoundingClientRect(); return { width: r.width, height: r.height }; }"
    )


def normalized_rect(page, selector):
    return page.locator(selector).evaluate(
        """el => {
            const board = document.querySelector('.festival-page__artboard').getBoundingClientRect();
            const r = el.getBoundingClientRect();
            const scale = board.width / 1440;
            return {
                left: (r.left - board.left) / scale,
                top: (r.top - board.top) / scale,
                width: r.width / scale,
                height: r.height / scale
            };
        }"""
    )


def assert_range(value, low, high, label):
    assert low <= value <= high, f"{label}: expected {low}..{high}, got {value:.1f}"


def pseudo_after(page, selector):
    return page.locator(selector).evaluate(
        """el => {
            const style = getComputedStyle(el, '::after');
            return {
                opacity: Number(style.opacity),
                transform: style.transform,
                transitionDuration: style.transitionDuration,
                borderWidth: style.borderWidth,
                backgroundColor: style.backgroundColor
            };
        }"""
    )


def focus_style(page, selector):
    return page.locator(selector).evaluate(
        """el => {
            el.focus();
            const style = getComputedStyle(el);
            return {
                outlineStyle: style.outlineStyle,
                outlineWidth: style.outlineWidth,
                outlineColor: style.outlineColor
            };
        }"""
    )


def keyboard_focus_style(page, selector):
    for _ in range(4):
        if page.evaluate("(selector) => document.activeElement?.matches(selector)", selector):
            break
        page.keyboard.press("Tab")

    assert page.evaluate("(selector) => document.activeElement?.matches(selector)", selector)
    return page.locator(selector).evaluate(
        """el => {
            const style = getComputedStyle(el);
            return {
                outlineStyle: style.outlineStyle,
                outlineWidth: style.outlineWidth,
                outlineColor: style.outlineColor
            };
        }"""
    )


def close_open_dialogs(page):
    page.keyboard.press("Escape")
    page.wait_for_timeout(120)
    page.evaluate(
        """() => document.querySelectorAll('dialog[open]').forEach((dialog) => dialog.close())"""
    )


def test_every_hotspot_has_precise_geometry_and_hover_feedback(browser):
    page, errors = new_page(browser)

    assert page.locator(".hotspot").count() == len(ALL_HOTSPOTS)

    for selector, (min_width, max_width) in TEXT_TARGETS.items():
        rect = normalized_rect(page, selector)
        assert_range(rect["width"], min_width, max_width, f"{selector} width")
        assert rect["height"] <= 52, f"{selector} text target is too tall: {rect['height']:.1f}"

    for selector, (min_width, max_width, min_height, max_height) in CONTROL_TARGETS.items():
        rect = normalized_rect(page, selector)
        assert_range(rect["width"], min_width, max_width, f"{selector} width")
        assert_range(rect["height"], min_height, max_height, f"{selector} height")

    for selector, (min_left, max_left, min_top, max_top) in POSITION_TARGETS.items():
        rect = normalized_rect(page, selector)
        assert_range(rect["left"], min_left, max_left, f"{selector} left")
        assert_range(rect["top"], min_top, max_top, f"{selector} top")

    for selector in ALL_HOTSPOTS:
        page.locator(selector).hover()
        page.wait_for_timeout(280)
        after = pseudo_after(page, selector)
        assert after["opacity"] >= 0.9, f"{selector} does not reveal hover feedback"

        focus = focus_style(page, selector)
        assert focus["outlineStyle"] != "none", f"{selector} lacks focus outline"
        assert focus["outlineWidth"] not in ("0px", "0"), f"{selector} focus outline is invisible"

    assert not errors
    page.close()


def test_every_hotspot_click_behavior_and_dialog_motion(browser):
    page, errors = new_page(browser)

    for selector in [
        ".hotspot--dogs",
        ".hotspot--partners",
        ".hotspot--market",
        ".hotspot--shelter",
        ".hotspot--faq",
        ".hotspot--contacts",
        ".hotspot--menu-dogs",
        ".hotspot--menu-activities",
        ".hotspot--menu-market",
        ".hotspot--menu-shelter",
        ".hotspot--menu-djs",
        ".hotspot--menu-faq",
    ]:
        page.evaluate("window.scrollTo(0, 0)")
        page.locator(selector).click()
        page.wait_for_timeout(360)
        assert page.evaluate("window.scrollY") > 0, f"{selector} did not scroll to its section"

    page.evaluate("window.scrollTo(0, 0)")
    active_before = page.locator(".dog-card-hotspot.is-active").get_attribute("data-dog")
    page.locator(".hotspot--cards-next").click()
    page.wait_for_timeout(100)
    active_after = page.locator(".dog-card-hotspot.is-active").get_attribute("data-dog")
    assert active_before != active_after

    for selector, dog in [
        (".hotspot--klepa", "dog-klepa"),
        (".hotspot--belka", "dog-belka"),
        (".hotspot--tolik", "dog-tolik"),
        (".hotspot--persey", "dog-persey"),
    ]:
        page.locator(selector).click()
        page.wait_for_selector(".dog-modal[open]")
        assert dog in page.locator(".dog-modal__image").get_attribute("src")
        page.locator(".dog-modal__close").hover()
        close_focus = keyboard_focus_style(page, ".dog-modal__close")
        assert close_focus["outlineStyle"] != "none"
        page.locator(".dog-modal__close").click()
        page.wait_for_function("!document.querySelector('.dog-modal').open", timeout=1000)

    for selector in [
        ".hotspot--activity-1",
        ".hotspot--activity-2",
        ".hotspot--activity-3",
        ".hotspot--activity-4",
        ".hotspot--activity-5",
        ".hotspot--activity-6",
        ".hotspot--partners-row",
        ".hotspot--market-logos",
        ".hotspot--shelter-site",
        ".hotspot--contact-1",
        ".hotspot--contact-2",
        ".hotspot--contact-3",
        ".hotspot--contact-4",
    ]:
        page.locator(selector).click()
        page.wait_for_selector(".info-modal[open]")
        assert page.locator(".info-modal__text").inner_text().strip()
        page.locator(".info-modal__close").hover()
        close_focus = keyboard_focus_style(page, ".info-modal__close")
        assert close_focus["outlineStyle"] != "none"
        page.locator(".info-modal__close").click()
        page.wait_for_function("!document.querySelector('.info-modal').open", timeout=1000)

    for selector in [
        ".hotspot--faq-1",
        ".hotspot--faq-2",
        ".hotspot--faq-3",
        ".hotspot--faq-4",
        ".hotspot--faq-5",
        ".hotspot--faq-6",
    ]:
        page.locator(selector).click()
        assert page.locator(selector).get_attribute("aria-expanded") == "true"
        assert page.locator(".faq-panel.is-open").is_visible()
        page.locator(selector).click()
        assert page.locator(selector).get_attribute("aria-expanded") == "false"

    page.locator(".hotspot--activity-1").click()
    page.wait_for_selector(".info-modal[open]")
    page.keyboard.press("Escape")
    page.wait_for_function("!document.querySelector('.info-modal').open", timeout=1000)

    assert not errors
    page.close()


@pytest.mark.parametrize("width,height", [(1440, 1000), (390, 844)])
def test_layout_has_no_horizontal_scroll_and_all_targets_are_clickable(browser, width, height):
    page, errors = new_page(browser, width=width, height=height)
    board = artboard_rect(page)
    assert board["width"] <= width
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1")

    for selector in ALL_HOTSPOTS:
        try:
            page.locator(selector).hover(timeout=1500)
        except PlaywrightTimeoutError as exc:
            pytest.fail(f"{selector} is not hoverable/clickable at {width}px: {exc}")

    close_open_dialogs(page)
    assert not errors
    page.close()


def test_reduced_motion_keeps_dialog_controls_immediate_and_usable(browser):
    page, errors = new_page(browser)
    page.emulate_media(reduced_motion="reduce")

    page.locator(".hotspot--klepa").click()
    page.wait_for_selector(".dog-modal[open]")
    page.locator(".dog-modal__close").click()
    page.wait_for_function("!document.querySelector('.dog-modal').open", timeout=500)

    duration = page.locator(".hotspot--klepa").evaluate(
        "el => getComputedStyle(el, '::after').transitionDuration"
    )
    assert duration in ("0.001s", "1ms")

    assert not errors
    page.close()
