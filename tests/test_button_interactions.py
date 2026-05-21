import os

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


BASE_URL = os.environ.get("QA_BASE_URL", "http://localhost:8092/")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


TEXT_TARGETS = {
    ".hotspot--dogs": (55, 65),
    ".hotspot--partners": (72, 82),
    ".hotspot--market": (52, 62),
    ".hotspot--shelter": (70, 80),
    ".hotspot--faq": (66, 76),
    ".hotspot--contacts": (72, 82),
    ".hotspot--menu-dogs": (690, 710),
    ".hotspot--menu-activities": (730, 750),
    ".hotspot--menu-market": (370, 390),
    ".hotspot--menu-shelter": (455, 475),
    ".hotspot--menu-djs": (180, 200),
    ".hotspot--menu-faq": (385, 405),
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
    ".hotspot--cards-prev": (75, 85, 58, 68),
    ".hotspot--cards-next": (75, 85, 58, 68),
    ".hotspot--partner-award": (185, 200, 60, 72),
    ".hotspot--partner-mrkranch": (170, 182, 95, 106),
    ".hotspot--partner-mnyams": (172, 184, 118, 128),
    ".hotspot--partner-ivsanbernard": (240, 255, 52, 64),
    ".hotspot--partner-craftia": (245, 258, 88, 100),
    ".hotspot--hvost-logo": (345, 355, 218, 230),
    ".hotspot--market-logos": (920, 955, 300, 330),
    ".hotspot--shelter-site": (240, 300, 40, 70),
}


POSITION_TARGETS = {
    ".hotspot--dogs": (428, 432, 60, 64),
    ".hotspot--partners": (554, 558, 60, 64),
    ".hotspot--market": (700, 704, 60, 64),
    ".hotspot--shelter": (822, 826, 60, 64),
    ".hotspot--faq": (965, 969, 60, 64),
    ".hotspot--contacts": (1105, 1109, 60, 64),
    ".hotspot--menu-dogs": (370, 374, 984, 992),
    ".hotspot--menu-activities": (352, 356, 1054, 1062),
    ".hotspot--menu-market": (529, 533, 1132, 1140),
    ".hotspot--menu-shelter": (488, 492, 1204, 1212),
    ".hotspot--menu-djs": (623, 627, 1283, 1291),
    ".hotspot--menu-faq": (522, 526, 1354, 1362),
    ".hotspot--partner-award": (122, 132, 4165, 4180),
    ".hotspot--partner-mrkranch": (403, 413, 4145, 4160),
    ".hotspot--partner-mnyams": (638, 648, 4118, 4132),
    ".hotspot--partner-ivsanbernard": (856, 866, 4168, 4182),
    ".hotspot--partner-craftia": (1126, 1136, 4145, 4160),
    ".hotspot--hvost-logo": (540, 550, 3383, 3396),
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
        max_height = 82 if "menu" in selector else 52
        assert rect["height"] <= max_height, f"{selector} text target is too tall: {rect['height']:.1f}"

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
        ".hotspot--market-logos",
        ".hotspot--contact-1",
        ".hotspot--contact-3",
    ]:
        page.locator(selector).click()
        page.wait_for_selector(".info-modal[open]")
        assert page.locator(".info-modal__text").inner_text().strip()
        page.locator(".info-modal__close").hover()
        close_focus = keyboard_focus_style(page, ".info-modal__close")
        assert close_focus["outlineStyle"] != "none"
        page.locator(".info-modal__close").click()
        page.wait_for_function("!document.querySelector('.info-modal').open", timeout=1000)

    external_links = {
        ".hotspot--partner-award": "https://vk.ru/award",
        ".hotspot--partner-mrkranch": "https://vk.com/mrkranch",
        ".hotspot--partner-mnyams": "https://vk.com/mnyams",
        ".hotspot--partner-ivsanbernard": "https://vk.com/ivsanbernardrus_official",
        ".hotspot--partner-craftia": "https://vk.com/craftia",
        ".hotspot--hvost-logo": "https://t.me/hvost_news",
        ".hotspot--shelter-site": "https://dogport.ru/",
        ".hotspot--contact-2": "https://dogport.ru/",
        ".hotspot--contact-4": "https://t.me/hvost_news",
    }

    for selector, href in external_links.items():
        assert page.locator(selector).get_attribute("href") == href
        assert page.locator(selector).get_attribute("target") == "_blank"
        assert "noopener" in page.locator(selector).get_attribute("rel")

    for selector in external_links:
        page.locator(selector).hover()
        page.wait_for_timeout(280)
        after = pseudo_after(page, selector)
        assert after["opacity"] >= 0.9, f"{selector} does not reveal link hover feedback"

    for index, selector in enumerate([
        ".faq-item:nth-child(1) .faq-item__button",
        ".faq-item:nth-child(2) .faq-item__button",
        ".faq-item:nth-child(3) .faq-item__button",
        ".faq-item:nth-child(4) .faq-item__button",
        ".faq-item:nth-child(5) .faq-item__button",
        ".faq-item:nth-child(6) .faq-item__button",
    ], start=1):
        page.locator(selector).click()
        assert page.locator(selector).get_attribute("aria-expanded") == "true"
        page.wait_for_timeout(320)
        assert page.locator(f".faq-item:nth-child({index}).is-open .faq-item__answer").is_visible()
        page.locator(selector).click()
        assert page.locator(selector).get_attribute("aria-expanded") == "false"

    page.locator(".hotspot--market-logos").click()
    page.wait_for_selector(".info-modal[open]")
    page.keyboard.press("Escape")
    page.wait_for_function("!document.querySelector('.info-modal').open", timeout=1000)

    assert not errors
    page.close()


def test_faq_accordion_matches_collapsed_and_expanded_behavior(browser):
    page, errors = new_page(browser)

    assert page.locator(".faq-section").is_visible()
    assert page.locator(".faq-item").count() == 6
    assert page.locator(".faq-panel").count() == 0

    for button in page.locator(".faq-item__button").all():
        assert button.get_attribute("aria-expanded") == "false"

    page.locator(".faq-item__button").first.hover()
    mark_color = page.locator(".faq-item__mark").first.evaluate(
        "el => getComputedStyle(el, '::before').backgroundColor"
    )
    assert mark_color == "rgb(0, 139, 21)"

    for button in page.locator(".faq-item__button").all():
        button.click()
        assert button.get_attribute("aria-expanded") == "true"

    assert page.locator(".faq-item.is-open").count() == 6
    assert page.locator(".faq-item.is-open .faq-item__answer p").count() == 6
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


def test_scroll_top_button_follows_page_and_returns_to_top(browser):
    page, errors = new_page(browser)

    assert page.locator(".scroll-top").evaluate("el => !el.classList.contains('is-visible')")

    page.evaluate("window.scrollTo(0, 1800)")
    page.wait_for_function("document.querySelector('.scroll-top').classList.contains('is-visible')")
    assert page.locator(".scroll-top img").get_attribute("src") == "assets/images/figma-final/scroll-top-arrow.png"

    page.locator(".scroll-top").hover()
    button = page.locator(".scroll-top").evaluate(
        """el => {
            const r = el.getBoundingClientRect();
            return {
                position: getComputedStyle(el).position,
                width: r.width,
                height: r.height,
                rightGap: window.innerWidth - r.right,
                bottomGap: window.innerHeight - r.bottom
            };
        }"""
    )
    assert button["position"] == "fixed"
    assert 56 <= button["width"] <= 86
    assert 56 <= button["height"] <= 86
    assert 12 <= button["rightGap"] <= 52
    assert 12 <= button["bottomGap"] <= 52

    page.locator(".scroll-top").click()
    page.wait_for_function("window.scrollY < 5", timeout=1800)

    assert not errors
    page.close()
