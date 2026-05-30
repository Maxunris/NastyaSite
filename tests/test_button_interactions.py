import os
from pathlib import Path

import pytest
from PIL import Image
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


BASE_URL = os.environ.get("QA_BASE_URL", "http://localhost:8092/")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MOBILE_ARTWORK_PATH = Path("assets/images/figma-2026/mobile/site-full-mobile.png")
INDEX_PATH = Path("index.html")

DOGS = [
    "klepa",
    "belka",
    "tolik",
    "persey",
    "alya",
    "johnny",
    "kesha",
    "maylo",
    "sky",
    "taya",
    "elis",
    "yasha",
]

BRAND_LINKS = {
    "plushki": "https://petvkus.ru",
    "sobakamama": "https://sobakamama.shop",
    "sobakin": "https://sobakin-shop.ru",
    "shaggy-dog": "https://shaggydog.ru",
    "derzhis-menya": "https://t.me/derzhismenya",
    "hug-me-dog": "https://hugmedog.ru",
}

BRAND_MOBILE_FILES = {
    "plushki": "Group-123-plushki.png",
    "sobakamama": "Group-124-sobakamama.png",
    "sobakin": "Group-125-sobakin.png",
    "shaggy-dog": "Group-121-shaggy-dog.png",
    "derzhis-menya": "Group-122-derzhis-menya.png",
    "hug-me-dog": "Group-120-hug-me-dog.png",
}

BRAND_DESKTOP_FILES = {
    "plushki": "Group 105.png",
    "sobakamama": "Group 96.png",
    "sobakin": "Group 83.png",
    "shaggy-dog": "Group 64.png",
    "derzhis-menya": "Group 67.png",
    "hug-me-dog": "Group 63.png",
}

MOBILE_BRAND_VISUAL_POINTS = {
    "hug-me-dog": (393, 14265),
    "shaggy-dog": (393, 14505),
    "derzhis-menya": (393, 14760),
    "sobakamama": (393, 15140),
    "sobakin": (393, 15415),
    "plushki": (393, 15700),
}

EVENT_SLIDE_FILES = [
    "rbTVTeycB2U8paixWNAPHVwCGOsGAzZ0FAYRZ1dPS46CNMb_u1CqoSNGbIfHcfZBBo 1.png",
    "unnamed (1) (1) 1.png",
    "unnamed (2) (1) 1.png",
]

CONTACT_LINKS = {
    ".hotspot--contact-1": "https://t.me/DogportMSK",
    ".hotspot--contact-2": "https://dogport.ru/",
    ".hotspot--contact-3": "https://t.me/danilovskymarket",
    ".hotspot--contact-4": "https://t.me/hvost_news",
    ".hotspot--contact-5": "https://t.me/anastasia_sabanina",
}

CONTACT_UNDERLINES = {
    ".hotspot--contact-1": (-9, -7, 208, 211),
    ".hotspot--contact-2": (-9, -7, 208, 211),
    ".hotspot--contact-3": (-23, -21, 208, 211),
    ".hotspot--contact-4": (-9, -7, 208, 212),
    ".hotspot--contact-5": (-26, -24, 203, 205),
}

MENU_TARGETS = {
    ".hotspot--menu-dogs": "#dogs",
    ".hotspot--menu-activities": "#activities",
    ".hotspot--menu-market": "#market",
    ".hotspot--menu-shelter": "#shelter",
    ".hotspot--menu-djs": "#djs",
    ".hotspot--menu-faq": "#faq",
}

MOBILE_MENU_VISUAL_POINTS = {
    "#dogs": (389, 1830),
    "#activities": (388, 1910),
    "#market": (389, 1992),
    "#shelter": (389, 2072),
    "#djs": (387, 2152),
    "#faq": (388, 2230),
}

DJ_LINKS = {
    "maksim": "https://t.me/tochnodj",
    "stepan": "https://t.me/nepal_prod",
}

DOGS_CONTACT_LINK = "https://t.me/marina_dogport"

HEADER_LOGO_LINKS = {
    ".header-logo-link--danilovsky": "https://t.me/danilovskymarket",
    ".header-logo-link--dogport": "https://dogport.ru/",
    ".header-logo-link--hvost-news": "https://t.me/hvost_news",
}

BRAND_RECTS = {
    "shaggy-dog": (270, 285, 7190, 7205),
    "derzhis-menya": (660, 675, 7118, 7132),
    "hug-me-dog": (965, 980, 7152, 7168),
    "sobakin": (452, 468, 7320, 7336),
    "sobakamama": (836, 852, 7328, 7344),
    "plushki": (620, 635, 7446, 7462),
}

PARTNER_RECTS = {
    ".hotspot--partner-award": (135, 150, 4740, 4755),
    ".hotspot--partner-mrkranch": (402, 418, 4716, 4732),
    ".hotspot--partner-mnyams": (640, 655, 4698, 4713),
    ".hotspot--partner-ivsanbernard": (858, 875, 4742, 4757),
    ".hotspot--partner-craftia": (1124, 1140, 4712, 4728),
}


def test_mobile_artwork_leaves_faq_area_blank_for_live_html():
    image = Image.open(MOBILE_ARTWORK_PATH).convert("RGB")
    assert image.size == (786, 20402)

    dark_pixels = 0
    for y in range(18450, 19320):
        for x in range(40, 735):
            r, g, b = image.getpixel((x, y))
            if r < 55 and g < 55 and b < 55:
                dark_pixels += 1

    assert dark_pixels == 0


def test_mobile_artwork_contacts_wave_starts_close_to_live_faq():
    image = Image.open(MOBILE_ARTWORK_PATH).convert("RGB")

    green_wave_start = None
    full_green_start = None
    for y in range(19000, 19600):
        green_pixels = 0
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            if g > 90 and r < 80 and b < 90:
                green_pixels += 1
        if green_pixels > 10:
            green_wave_start = green_wave_start or y
        if green_pixels == image.width:
            full_green_start = full_green_start or y
        if green_wave_start and full_green_start:
            break

    assert green_wave_start is not None
    assert full_green_start is not None
    assert 19310 <= green_wave_start <= 19340
    assert full_green_start - green_wave_start >= 90

    top_green_pixels = 0
    for x in range(image.width):
        r, g, b = image.getpixel((x, green_wave_start))
        if g > 90 and r < 80 and b < 90:
            top_green_pixels += 1
    assert top_green_pixels <= 30


def test_mobile_artwork_contacts_bottom_has_no_stray_white_stroke():
    image = Image.open(MOBILE_ARTWORK_PATH).convert("RGB")

    for y in range(20255, 20340):
        white_pixels = 0
        for x in range(120, 660):
            r, g, b = image.getpixel((x, y))
            if r > 210 and g > 210 and b > 210:
                white_pixels += 1

        assert white_pixels < 40


def test_index_busts_mobile_faq_css_cache():
    html = INDEX_PATH.read_text(encoding="utf-8")

    assert 'href="styles.css?v=figma-2026-52"' in html


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


def close_modal(page):
    if page.locator(".dog-modal[open]").count():
        page.locator(".dog-modal__close").click()
        page.wait_for_function("!document.querySelector('.dog-modal').open", timeout=1000)


def click_mobile_artwork_point(page, natural_x, natural_y):
    page.evaluate(
        """([, y]) => {
            const board = document.querySelector('.festival-page__artboard');
            const scale = board.getBoundingClientRect().width / 786;
            window.scrollTo({ top: Math.max(0, y * scale - window.innerHeight / 2), behavior: 'instant' });
        }""",
        [natural_x, natural_y],
    )
    page.wait_for_timeout(80)
    point = page.evaluate(
        """([x, y]) => {
            const board = document.querySelector('.festival-page__artboard').getBoundingClientRect();
            const scale = board.width / 786;
            return { x: board.left + x * scale, y: board.top + y * scale };
        }""",
        [natural_x, natural_y],
    )
    page.mouse.click(point["x"], point["y"])


def pseudo_after(page, selector):
    return page.locator(selector).evaluate(
        """el => {
            const style = getComputedStyle(el, '::after');
            return {
                opacity: Number(style.opacity),
                transform: style.transform,
                transitionProperty: style.transitionProperty,
                backgroundImage: style.backgroundImage,
                borderWidth: style.borderWidth,
                left: style.left,
                right: style.right,
                bottom: style.bottom,
                display: style.display,
                height: style.height,
                width: style.width
            };
        }"""
    )


def dog_frame_rects(page):
    return page.evaluate(
        """() => {
            const viewport = document.querySelector('.dog-carousel__viewport').getBoundingClientRect();
            const buttons = [...document.querySelectorAll('.dog-frame-button')].map((button) => {
                const r = button.getBoundingClientRect();
                return { dog: button.dataset.dog, left: r.left, right: r.right, width: r.width };
            });
            return { viewport: { left: viewport.left, right: viewport.right }, buttons };
        }"""
    )


def test_page_uses_new_full_artwork_without_flattening_live_layers(browser):
    page, errors = new_page(browser)

    assert page.locator(".festival-page__image").get_attribute("src").split("?")[0] == "assets/images/figma-2026/site-full.png"
    assert page.locator(".festival-page__image").get_attribute("height") == "10264"
    assert page.locator(".festival-page__hotspots").count() == 1
    assert page.locator(".faq-section").count() == 1
    assert page.locator(".faq-item__button").count() == 6
    assert page.locator(".dog-carousel").count() == 1
    assert page.locator(".dog-frame-button").count() == 22
    assert page.locator(".dog-carousel__page").count() == 6

    assert not errors
    page.close()


def test_mobile_uses_updated_full_artwork_dimensions(browser):
    page, errors = new_page(browser, width=390, height=844)

    image = page.locator(".festival-page__image")
    assert image.evaluate("img => img.currentSrc").split("?")[0].endswith(
        "assets/images/figma-2026/mobile/site-full-mobile.png"
    )
    assert image.evaluate("img => img.naturalWidth") == 786
    assert image.evaluate("img => img.naturalHeight") == 20402

    assert not errors
    page.close()


def test_header_logos_are_plain_links_without_hover_animation(browser):
    page, errors = new_page(browser)

    for selector, href in HEADER_LOGO_LINKS.items():
        link = page.locator(selector)
        assert link.get_attribute("href") == href
        assert link.get_attribute("target") == "_blank"
        assert "noopener" in link.get_attribute("rel")
        link.hover()
        page.wait_for_timeout(180)
        state = link.evaluate(
            """el => ({
                before: getComputedStyle(el, '::before').content,
                after: getComputedStyle(el, '::after').content,
                transform: getComputedStyle(el).transform
            })"""
        )
        assert state["before"] == "none"
        assert state["after"] == "none"
        assert state["transform"] in ("none", "matrix(1, 0, 0, 1, 0, 0)")

    assert not errors
    page.close()


def test_dog_carousel_arrows_move_track_and_each_dog_opens_matching_card(browser):
    page, errors = new_page(browser)

    page.locator(".dog-carousel").scroll_into_view_if_needed()
    shelter_contact = page.locator(".hotspot--dogs-contact-shelter")
    assert shelter_contact.get_attribute("href") == DOGS_CONTACT_LINK
    shelter_contact.hover()
    page.wait_for_timeout(220)
    shelter_underline = pseudo_after(page, ".hotspot--dogs-contact-shelter")
    shelter_rect = normalized_rect(page, ".hotspot--dogs-contact-shelter")
    assert shelter_underline["display"] != "none"
    assert shelter_underline["opacity"] >= 0.9
    assert shelter_underline["height"] == "3px"
    assert_range(float(shelter_underline["bottom"].replace("px", "")), -27, -23, "shelter contact underline bottom")
    assert_range(float(shelter_underline["left"].replace("px", "")), 2, 4, "shelter contact underline left")
    assert_range(float(shelter_underline["width"].replace("px", "")), shelter_rect["width"] - 19, shelter_rect["width"] - 17, "shelter contact underline width")

    before = page.locator(".dog-carousel__track").evaluate("el => getComputedStyle(el).transform")
    page.locator(".hotspot--cards-next").click()
    page.wait_for_timeout(520)
    after = page.locator(".dog-carousel__track").evaluate("el => getComputedStyle(el).transform")
    assert before != after
    assert page.locator(".dog-carousel__page.is-active").get_attribute("data-dog-page") == "1"

    page.locator(".hotspot--cards-prev").click()
    page.wait_for_timeout(520)
    reset = page.locator(".dog-carousel__track").evaluate("el => getComputedStyle(el).transform")
    assert reset.startswith("matrix(1, 0, 0, 1, 0")
    assert page.locator(".dog-carousel__page.is-active").get_attribute("data-dog-page") == "0"

    for _ in range(2):
        page.locator(".hotspot--cards-next").click()
        page.wait_for_timeout(520)
    assert page.locator(".dog-carousel__page.is-active").get_attribute("data-dog-page") == "2"

    rects = dog_frame_rects(page)
    visible = [
        button for button in rects["buttons"]
        if button["right"] > rects["viewport"]["left"] + 4 and button["left"] < rects["viewport"]["right"] - 4
    ]
    assert [button["dog"] for button in visible] == ["sky", "taya", "elis", "yasha"]
    assert visible[0]["left"] >= rects["viewport"]["left"] - 1
    assert visible[-1]["right"] <= rects["viewport"]["right"] + 1

    page_two_transform = page.locator(".dog-carousel__track").evaluate("el => getComputedStyle(el).transform")
    page.locator("[data-dog='yasha']").hover()
    page.wait_for_timeout(120)
    hover_border = page.locator("[data-dog='yasha']").evaluate(
        "el => getComputedStyle(el, '::after').borderColor"
    )
    assert hover_border == "rgb(255, 255, 255)"
    page.locator("[data-dog='yasha']").click()
    page.wait_for_selector(".dog-modal[open]")
    assert page.locator(".dog-carousel__track").evaluate("el => getComputedStyle(el).transform") == page_two_transform
    close_modal(page)

    page.locator(".dog-carousel__page[data-dog-page='1']").click()
    page.wait_for_timeout(520)
    assert page.locator(".dog-carousel__page.is-active").get_attribute("data-dog-page") == "1"

    for page_index, dogs in enumerate([DOGS[0:4], DOGS[4:8], DOGS[8:12]]):
        page.evaluate("(pageIndex) => window.__debugDogPage = pageIndex", page_index)
        while True:
            rects = dog_frame_rects(page)
            visible_dogs = [
                button["dog"] for button in rects["buttons"]
                if button["right"] > rects["viewport"]["left"] + 4 and button["left"] < rects["viewport"]["right"] - 4
            ]
            if visible_dogs == dogs:
                break
            page.locator(".hotspot--cards-next").click()
            page.wait_for_timeout(520)

        for dog in dogs:
            button = page.locator(f"[data-dog='{dog}']")
            button.click()
            page.wait_for_selector(".dog-modal[open]")
            assert "dog-cards" in page.locator(".dog-modal__image").get_attribute("src")
            assert dog in page.locator(".dog-modal__image").get_attribute("alt").lower()
            close_modal(page)

    assert not errors
    page.close()


def test_dog_carousel_desktop_arrows_use_css_icons_without_raster_assets(browser):
    page, errors = new_page(browser, width=1440, height=1000)

    prev_bg = page.locator(".hotspot--cards-prev").evaluate("el => getComputedStyle(el).backgroundImage")
    next_bg = page.locator(".hotspot--cards-next").evaluate("el => getComputedStyle(el).backgroundImage")
    prev_before = page.locator(".hotspot--cards-prev").evaluate("el => getComputedStyle(el, '::before').content")
    next_before = page.locator(".hotspot--cards-next").evaluate("el => getComputedStyle(el, '::before').content")
    prev_after = page.locator(".hotspot--cards-prev").evaluate("el => getComputedStyle(el, '::after').content")
    next_after = page.locator(".hotspot--cards-next").evaluate("el => getComputedStyle(el, '::after').content")

    assert prev_bg == "none"
    assert next_bg == "none"
    assert "carousel-arrow-left.png" not in prev_bg
    assert "carousel-arrow-right.png" not in next_bg
    assert prev_before == '""'
    assert next_before == '""'
    assert prev_after == "none"
    assert next_after == "none"

    assert not errors
    page.close()


def test_brand_cards_use_six_updated_partners_and_preserve_hover_motion(browser):
    page, errors = new_page(browser)

    assert page.locator(".brand-card-hotspot").count() == 6

    for brand, href in BRAND_LINKS.items():
        selector = f"[data-brand='{brand}']"
        rect = normalized_rect(page, selector)
        min_left, max_left, min_top, max_top = BRAND_RECTS[brand]
        assert_range(rect["left"], min_left, max_left, f"{brand} left")
        assert_range(rect["top"], min_top, max_top, f"{brand} top")

        page.locator(selector).scroll_into_view_if_needed()
        page.locator(selector).hover()
        page.wait_for_timeout(480)
        hover = pseudo_after(page, selector)
        assert hover["opacity"] >= 0.9
        assert "transform" in hover["transitionProperty"]
        assert "url(" not in hover["backgroundImage"]
        assert_range(float(hover["bottom"].replace("px", "")), -18, -12, f"{brand} underline bottom")
        if brand == "derzhis-menya":
            assert_range(float(hover["left"].replace("px", "")), 8, 10, "derzhis underline left")
            assert_range(float(hover["width"].replace("px", "")), 109, 112, "derzhis underline width")

        page.locator(selector).click()
        page.wait_for_selector(".dog-modal[open]")
        src = page.locator(".dog-modal__image").get_attribute("src")
        assert "brand-cards/" in src
        assert BRAND_DESKTOP_FILES[brand] in src
        assert page.locator(".dog-modal").evaluate("el => el.classList.contains('dog-modal--brand')")
        assert page.locator(".dog-modal__image").evaluate("el => getComputedStyle(el).borderRadius") in (
            "48px",
            "48px 48px 48px 48px",
        )
        assert page.locator(".dog-modal__brand-link.is-visible").is_visible()
        assert page.locator(".dog-modal__brand-link").get_attribute("href") == href
        close_modal(page)

    assert not errors
    page.close()


def test_partner_logo_hotspots_are_aligned_and_do_not_duplicate_logos(browser):
    page, errors = new_page(browser)

    for selector, (min_left, max_left, min_top, max_top) in PARTNER_RECTS.items():
        rect = normalized_rect(page, selector)
        assert_range(rect["left"], min_left, max_left, f"{selector} left")
        assert_range(rect["top"], min_top, max_top, f"{selector} top")
        page.locator(selector).scroll_into_view_if_needed()
        page.locator(selector).hover()
        page.wait_for_timeout(360)
        hover = pseudo_after(page, selector)
        assert hover["opacity"] >= 0.9
        assert "url(" not in hover["backgroundImage"]
        assert_range(float(hover["bottom"].replace("px", "")), -18, -14, f"{selector} underline bottom")

    page.locator(".hotspot--hvost-logo").scroll_into_view_if_needed()
    page.locator(".hotspot--hvost-logo").hover()
    page.wait_for_timeout(360)
    hvost_hover = pseudo_after(page, ".hotspot--hvost-logo")
    assert hvost_hover["opacity"] >= 0.9
    assert_range(float(hvost_hover["bottom"].replace("px", "")), 3, 5, "hvost logo underline bottom")

    assert not errors
    page.close()


def test_desktop_uses_single_photozone_card_from_full_artwork(browser):
    page, errors = new_page(browser, width=1440, height=1000)

    photozone_patch = page.locator(".schedule-photozone-fix")
    assert photozone_patch.evaluate("el => getComputedStyle(el).display") == "none"
    assert page.locator(".event-carousel").evaluate("el => getComputedStyle(el).display") == "none"

    assert not errors
    page.close()


def test_second_menu_hotspots_align_to_visible_items_and_scroll_to_sections(browser):
    page, errors = new_page(browser, width=1440, height=1000)

    expected_tops = {
        ".hotspot--menu-dogs": (970, 1030),
        ".hotspot--menu-activities": (1040, 1105),
        ".hotspot--menu-market": (1125, 1185),
        ".hotspot--menu-shelter": (1195, 1260),
        ".hotspot--menu-djs": (1275, 1345),
        ".hotspot--menu-faq": (1350, 1425),
    }

    for selector, target in MENU_TARGETS.items():
        rect = normalized_rect(page, selector)
        min_top, max_top = expected_tops[selector]
        assert_range(rect["top"], min_top, max_top, f"{selector} desktop top")

        page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
        page.locator(selector).click()
        page.wait_for_function(
            """targetSelector => {
                const target = document.querySelector(targetSelector);
                if (!target) return false;
                const rect = target.getBoundingClientRect();
                return rect.top >= -20 && rect.top <= 280;
            }""",
            arg=target,
            timeout=2400,
        )

    assert not errors
    page.close()


def test_desktop_second_menu_uses_green_pill_hover_from_original_design(browser):
    page, errors = new_page(browser, width=1440, height=1000)

    selector = ".hotspot--menu-dogs"
    mask = page.locator(".festival-page__artboard").evaluate(
        """el => {
            const before = getComputedStyle(el, '::before');
            return {
                background: before.backgroundColor,
                height: before.height,
                width: before.width
            };
        }"""
    )
    assert mask["background"] == "rgb(255, 255, 255)"
    assert mask["height"] != "auto"
    assert mask["width"] != "auto"

    idle = page.locator(selector).evaluate(
        """el => {
            const after = getComputedStyle(el, '::after');
            return {
                color: getComputedStyle(el).color,
                fontSize: getComputedStyle(el).fontSize,
                background: after.backgroundColor,
                opacity: Number(after.opacity)
            };
        }"""
    )
    assert idle["color"] == "rgb(0, 139, 21)"
    assert idle["fontSize"] != "0px"
    assert idle["opacity"] == 0

    page.locator(selector).hover()
    page.wait_for_timeout(360)
    hover = page.locator(selector).evaluate(
        """el => {
            const after = getComputedStyle(el, '::after');
            return {
                color: getComputedStyle(el).color,
                fontSize: getComputedStyle(el).fontSize,
                background: after.backgroundColor,
                height: after.height,
                opacity: Number(after.opacity),
                transform: after.transform,
                borderRadius: after.borderRadius
            };
        }"""
    )

    assert hover["color"] == "rgb(255, 255, 255)"
    assert hover["fontSize"] != "0px"
    assert hover["background"] == "rgb(0, 139, 21)"
    assert hover["height"] != "4px"
    assert hover["opacity"] >= 0.95
    assert hover["borderRadius"] == "999px"

    assert not errors
    page.close()


def test_mobile_second_menu_items_are_clickable_and_scroll_to_sections(browser):
    page, errors = new_page(browser, width=390, height=844)

    for selector, target in MENU_TARGETS.items():
        page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
        page.locator(selector).click()
        page.wait_for_function(
            """targetSelector => {
                const target = document.querySelector(targetSelector);
                if (!target) return false;
                const rect = target.getBoundingClientRect();
                return rect.top >= -20 && rect.top <= 360;
            }""",
            arg=target,
            timeout=2400,
        )

    assert not errors
    page.close()


def test_mobile_second_menu_visible_text_points_scroll_to_correct_sections(browser):
    page, errors = new_page(browser, width=390, height=844)

    for target, point in MOBILE_MENU_VISUAL_POINTS.items():
        page.evaluate("window.scrollTo({ top: 0, behavior: 'instant' })")
        click_mobile_artwork_point(page, *point)
        page.wait_for_function(
            """targetSelector => {
                const target = document.querySelector(targetSelector);
                if (!target) return false;
                const rect = target.getBoundingClientRect();
                return rect.top >= -20 && rect.top <= 360;
            }""",
            arg=target,
            timeout=2400,
        )

    assert not errors
    page.close()


def test_page_accepts_user_scroll_immediately_after_domcontentloaded(browser):
    page = browser.new_page(viewport={"width": 390, "height": 844})
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.goto(BASE_URL, wait_until="domcontentloaded")

    assert page.evaluate("document.documentElement.scrollHeight > window.innerHeight * 4")
    assert page.evaluate("getComputedStyle(document.body).overflowY") != "hidden"

    page.mouse.move(200, 400)
    for _ in range(8):
        page.mouse.wheel(0, 700)
        page.wait_for_timeout(60)
        if page.evaluate("window.scrollY") > 100:
            break

    assert page.evaluate("window.scrollY") > 100

    assert not errors
    page.close()


def test_mobile_dog_carousel_does_not_paint_a_visible_live_frame(browser):
    page, errors = new_page(browser, width=390, height=844)

    state = page.locator(".dog-carousel").evaluate(
        """el => ({
            background: getComputedStyle(el).backgroundColor,
            overflow: getComputedStyle(el).overflow,
            borderRadius: getComputedStyle(el).borderRadius,
            boxShadow: getComputedStyle(el).boxShadow
        })"""
    )

    assert state["background"] == "rgb(255, 255, 255)"
    assert state["overflow"] == "hidden"
    assert state["borderRadius"] == "0px"
    assert "rgb(255, 255, 255) 0px -12px 0px 12px" in state["boxShadow"]
    active_src = page.locator(".dog-frame-button.is-active img").get_attribute("src")
    assert "dog-frames/" in active_src
    assert "dog-frames-mobile-clean" not in active_src

    assert not errors
    page.close()


def test_mobile_dog_carousel_shows_only_active_frame_during_transition(browser):
    page, errors = new_page(browser, width=390, height=844)

    page.locator(".dog-carousel").scroll_into_view_if_needed()
    page.locator(".hotspot--cards-next").click()
    page.wait_for_timeout(80)

    visible_frames = page.locator(".dog-frame-button").evaluate_all(
        """buttons => buttons
            .filter((button) => {
                const style = getComputedStyle(button);
                const rect = button.getBoundingClientRect();
                return style.visibility !== 'hidden' && Number(style.opacity) > 0.05 && rect.width > 0 && rect.height > 0;
            })
            .map((button) => button.dataset.dog)"""
    )

    assert visible_frames == ["belka"]
    active_src = page.locator(".dog-frame-button.is-active img").get_attribute("src")
    assert "dog-frames/" in active_src
    assert "dog-frames-mobile-clean" not in active_src

    assert not errors
    page.close()


def test_mobile_partner_photo_arrows_cycle_live_image(browser):
    page, errors = new_page(browser, width=390, height=844)

    page.locator(".event-carousel").scroll_into_view_if_needed()
    image = page.locator(".event-carousel__image")
    prev_button = page.locator(".event-carousel__button--prev")
    next_button = page.locator(".event-carousel__button--next")

    assert image.get_attribute("src").endswith(EVENT_SLIDE_FILES[0])
    assert prev_button.is_visible()
    assert next_button.is_visible()

    next_button.click()
    page.wait_for_timeout(180)
    assert image.get_attribute("src").endswith(EVENT_SLIDE_FILES[1])

    next_button.click()
    page.wait_for_timeout(180)
    assert image.get_attribute("src").endswith(EVENT_SLIDE_FILES[2])

    prev_button.click()
    page.wait_for_timeout(180)
    assert image.get_attribute("src").endswith(EVENT_SLIDE_FILES[1])

    assert not errors
    page.close()


def test_mobile_faq_contacts_transition_reveals_green_wave(browser):
    page, errors = new_page(browser, width=390, height=844)

    transition = page.evaluate(
        """() => {
            const faq = document.querySelector('.faq-section');
            const contacts = document.querySelector('#contacts');
            const board = document.querySelector('.festival-page__artboard').getBoundingClientRect();
            const scale = board.width / 786;
            const lastFaqItem = [...document.querySelectorAll('.faq-item')].at(-1);
            const lastItem = lastFaqItem.getBoundingClientRect();
            return {
                faqBackground: getComputedStyle(faq).backgroundColor,
                faqBottom: faq.offsetTop + faq.offsetHeight,
                contactsTop: contacts.offsetTop,
                lastFaqItemBorder: getComputedStyle(lastFaqItem).borderBottomColor,
                lastFaqItemBottomNatural: (lastItem.bottom - board.top) / scale
            };
        }"""
    )

    assert transition["faqBackground"] == "rgba(0, 0, 0, 0)"
    assert transition["lastFaqItemBorder"] == "rgba(0, 0, 0, 0)"
    assert transition["lastFaqItemBottomNatural"] < 19360
    assert transition["faqBottom"] < transition["contactsTop"] - 55

    assert not errors
    page.close()


def test_mobile_all_brand_logos_open_their_own_cards(browser):
    page, errors = new_page(browser, width=390, height=844)

    for brand, href in BRAND_LINKS.items():
        selector = f"[data-brand='{brand}']"
        page.locator(selector).scroll_into_view_if_needed()
        page.locator(selector).click()
        page.wait_for_selector(".dog-modal[open]")
        src = page.locator(".dog-modal__image").get_attribute("src")
        assert "brand-cards-mobile" in src
        assert BRAND_MOBILE_FILES[brand] in src
        assert page.locator(".dog-modal__image").evaluate("img => img.naturalWidth") == 960
        if brand == "plushki":
            assert "Плюшки" in page.locator(".dog-modal__image").get_attribute("alt")
        brand_link = page.locator(".dog-modal__brand-link")
        assert brand_link.get_attribute("href") == href
        link_box = brand_link.bounding_box()
        image_box = page.locator(".dog-modal__image").bounding_box()
        assert link_box["width"] > image_box["width"] * 0.7
        assert link_box["y"] > image_box["y"] + image_box["height"] * 0.84
        assert brand_link.evaluate(
            """link => {
                const r = link.getBoundingClientRect();
                const topNode = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
                return topNode === link || link.contains(topNode);
            }"""
        )
        close_modal(page)

    assert not errors
    page.close()


def test_mobile_visible_brand_logos_open_matching_cards(browser):
    page, errors = new_page(browser, width=390, height=844)

    for brand, (natural_x, natural_y) in MOBILE_BRAND_VISUAL_POINTS.items():
        click_mobile_artwork_point(page, natural_x, natural_y)
        page.wait_for_selector(".dog-modal[open]")
        assert BRAND_MOBILE_FILES[brand] in page.locator(".dog-modal__image").get_attribute("src")
        assert page.locator(".dog-modal__brand-link").get_attribute("href") == BRAND_LINKS[brand]
        close_modal(page)

    assert not errors
    page.close()


def test_mobile_brand_modal_does_not_show_side_arrows(browser):
    page, errors = new_page(browser, width=390, height=844)

    page.locator("[data-brand='hug-me-dog']").scroll_into_view_if_needed()
    page.locator("[data-brand='hug-me-dog']").click()
    page.wait_for_selector(".dog-modal[open]")

    assert not page.locator(".dog-modal__brand-nav--prev").is_visible()
    assert not page.locator(".dog-modal__brand-nav--next").is_visible()
    close_modal(page)

    assert not errors
    page.close()


def test_artist_and_shelter_buttons_match_new_figma_positions(browser):
    page, errors = new_page(browser)

    artist = page.locator(".hotspot--artist-channel")
    assert artist.get_attribute("href") == "https://t.me/artemisialisa"
    assert artist.get_attribute("target") == "_blank"
    artist_rect = normalized_rect(page, ".hotspot--artist-channel")
    assert_range(artist_rect["left"], 300, 330, "artist left")
    assert_range(artist_rect["top"], 5720, 5760, "artist top")
    assert_range(artist_rect["width"], 250, 290, "artist width")

    shelter = page.locator(".hotspot--shelter-site")
    assert shelter.get_attribute("href") == "https://dogport.ru/"
    shelter_rect = normalized_rect(page, ".hotspot--shelter-site")
    assert_range(shelter_rect["left"], 560, 600, "shelter button left")
    assert_range(shelter_rect["top"], 8092, 8106, "shelter button top")

    assert not errors
    page.close()


def test_faq_stays_live_after_dj_section_and_contacts_include_all_questions_link(browser):
    page, errors = new_page(browser)

    shelter_top = page.locator("#shelter").evaluate("el => el.offsetTop")
    djs_top = page.locator("#djs").evaluate("el => el.offsetTop")
    faq_top = page.locator("#faq").evaluate("el => el.offsetTop")
    contacts_top = page.locator("#contacts").evaluate("el => el.offsetTop")
    assert shelter_top < djs_top < faq_top < contacts_top
    assert faq_top - djs_top > 800
    faq_mask = page.locator(".faq-section").evaluate(
        """el => {
            const before = getComputedStyle(el, '::before');
            return {
                background: before.backgroundColor,
                display: before.display,
                height: before.height,
                top: before.top,
                width: before.width
            };
        }"""
    )
    assert faq_mask["display"] == "block"
    assert faq_mask["background"] == "rgb(255, 255, 255)"
    assert_range(float(faq_mask["top"].replace("px", "")), -181, -179, "faq top mask")
    assert_range(float(faq_mask["height"].replace("px", "")), 179, 181, "faq mask height")
    assert_range(float(faq_mask["width"].replace("px", "")), 1439, 1441, "faq mask width")

    first_faq = page.locator(".faq-item__button").first
    assert first_faq.get_attribute("aria-expanded") == "false"
    first_faq.click()
    assert first_faq.get_attribute("aria-expanded") == "true"
    page.wait_for_timeout(320)
    assert page.locator(".faq-item.is-open .faq-item__answer p").first.is_visible()

    for selector, href in CONTACT_LINKS.items():
        assert page.locator(selector).get_attribute("href") == href
        page.locator(selector).scroll_into_view_if_needed()
        page.locator(selector).hover()
        page.wait_for_timeout(280)
        underline = pseudo_after(page, selector)
        left_min, left_max, width_min, width_max = CONTACT_UNDERLINES[selector]
        assert underline["opacity"] >= 0.9
        assert_range(float(underline["bottom"].replace("px", "")), -11, -9, f"{selector} underline bottom")
        assert_range(float(underline["left"].replace("px", "")), left_min, left_max, f"{selector} underline left")
        assert_range(float(underline["width"].replace("px", "")), width_min, width_max, f"{selector} underline width")

    contact_shelter = page.locator(".hotspot--contact-2").evaluate(
        """el => ({
            text: el.textContent,
            borderWidth: getComputedStyle(el).borderWidth,
            background: getComputedStyle(el).backgroundColor,
            backgroundImage: getComputedStyle(el).backgroundImage,
            color: getComputedStyle(el).color,
            fontSize: getComputedStyle(el).fontSize
        })"""
    )
    assert contact_shelter["text"] == "Сайт приюта"
    assert contact_shelter["borderWidth"] == "0px"
    assert contact_shelter["background"] == "rgba(0, 0, 0, 0)"
    assert contact_shelter["backgroundImage"] == "none"
    assert contact_shelter["color"] == "rgba(0, 0, 0, 0)"
    assert contact_shelter["fontSize"] == "0px"

    assert not errors
    page.close()


def test_dj_hotspots_open_new_cards_and_tg_links(browser):
    page, errors = new_page(browser)

    assert page.locator(".djs-section-art").count() == 1
    assert page.locator(".dj-card-hotspot").count() == 2

    for dj, href in DJ_LINKS.items():
        selector = f"[data-dj='{dj}']"
        rect = normalized_rect(page, selector)
        assert_range(rect["top"], 8715, 8730, f"{dj} dj top")
        if dj == "maksim":
            assert_range(rect["left"], 486, 502, "maksim dj left")
        else:
            assert_range(rect["left"], 752, 768, "stepan dj left")
        page.locator(selector).hover()
        page.wait_for_timeout(240)
        underline = pseudo_after(page, selector)
        assert_range(float(underline["bottom"].replace("px", "")), -11, -9, f"{dj} dj underline bottom")
        page.locator(selector).click()
        page.wait_for_selector(".dog-modal[open]")
        assert "/djs/" in page.locator(".dog-modal__image").get_attribute("src")
        assert page.locator(".dog-modal").evaluate("el => el.classList.contains('dog-modal--dj')")
        assert page.locator(".dog-modal__brand-link").get_attribute("href") == href
        close_modal(page)

    assert not errors
    page.close()


def test_desktop_dj_art_uses_clean_artwork_without_extra_patch(browser):
    page, errors = new_page(browser, width=1440, height=1000)

    assert page.locator(".djs-section-art").evaluate("el => getComputedStyle(el).display") != "none"
    assert page.locator(".djs-hole-fix").evaluate("el => getComputedStyle(el).display") == "none"

    assert not errors
    page.close()


def test_page_exposes_site_favicon_assets(browser):
    page, errors = new_page(browser, width=1440, height=1000)

    icons = page.locator("link[rel~='icon']").evaluate_all(
        """links => links.map(link => ({
            href: link.getAttribute('href'),
            type: link.getAttribute('type') || '',
            sizes: link.getAttribute('sizes') || ''
        }))"""
    )
    assert any(icon["href"] == "assets/images/favicon.svg" and icon["type"] == "image/svg+xml" for icon in icons)
    assert any(icon["href"] == "assets/images/favicon.png" and icon["type"] == "image/png" and icon["sizes"] == "any" for icon in icons)
    assert page.locator("link[rel='apple-touch-icon']").get_attribute("href") == "assets/images/favicon.png"

    assert not errors
    page.close()


@pytest.mark.parametrize("width,height", [(1440, 1000), (390, 844)])
def test_layout_has_no_horizontal_scroll_and_live_targets_are_clickable(browser, width, height):
    page, errors = new_page(browser, width=width, height=height)

    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth + 1")

    live_targets = [
        ".hotspot--dogs",
        ".hotspot--partners",
        ".hotspot--market",
        ".hotspot--shelter",
        ".hotspot--faq",
        ".hotspot--contacts",
        ".hotspot--cards-prev",
        ".hotspot--cards-next",
        ".hotspot--dogs-contact-shelter",
        ".hotspot--artist-channel",
        ".dog-frame-button",
        ".brand-card-hotspot",
        ".faq-item__button",
        *CONTACT_LINKS.keys(),
    ]

    if width <= 700:
        live_targets = [
            selector for selector in live_targets
            if selector
            not in {
                ".hotspot--dogs",
                ".hotspot--partners",
                ".hotspot--market",
                ".hotspot--shelter",
                ".hotspot--faq",
                ".hotspot--contacts",
                ".hotspot--artist-channel",
            }
        ]
        live_targets.extend(MENU_TARGETS.keys())

    for selector in live_targets:
        try:
            page.locator(selector).first.scroll_into_view_if_needed(timeout=4000)
            page.locator(selector).first.hover(timeout=4000)
        except PlaywrightTimeoutError as exc:
            pytest.fail(f"{selector} is not hoverable/clickable at {width}px: {exc}")

    assert not errors
    page.close()
