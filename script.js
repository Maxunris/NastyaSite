document.querySelectorAll('.dogs-section-clean').forEach((node) => node.remove());

const dogCards = {
  klepa: {
    name: 'Клёпа',
    frame: 'assets/images/figma-2026/dog-frames/Frame 6.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 70.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 108.png',
    alt: 'klepa, карточка Клёпы.',
  },
  belka: {
    name: 'Белка',
    frame: 'assets/images/figma-2026/dog-frames/Frame 7.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 65.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 106.png',
    alt: 'belka, карточка Белки.',
  },
  tolik: {
    name: 'Толик',
    frame: 'assets/images/figma-2026/dog-frames/Frame 8.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 69.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 107.png',
    alt: 'tolik, карточка Толика.',
  },
  persey: {
    name: 'Персей',
    frame: 'assets/images/figma-2026/dog-frames/Frame 9.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 82.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 110.png',
    alt: 'persey, карточка Персея.',
  },
  alya: {
    name: 'Аля',
    frame: 'assets/images/figma-2026/dog-frames/Аля.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 99.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 113.png',
    alt: 'alya, карточка Али.',
  },
  johnny: {
    name: 'Джонни',
    frame: 'assets/images/figma-2026/dog-frames/Джонни.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 98.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 112.png',
    alt: 'johnny, карточка Джонни.',
  },
  kesha: {
    name: 'Кеша',
    frame: 'assets/images/figma-2026/dog-frames/Кеша.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 103.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 117.png',
    alt: 'kesha, карточка Кеши.',
  },
  maylo: {
    name: 'Майло',
    frame: 'assets/images/figma-2026/dog-frames/Майло.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 100.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 114.png',
    alt: 'maylo, карточка Майло.',
  },
  sky: {
    name: 'Скай',
    frame: 'assets/images/figma-2026/dog-frames/Скай.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 145.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 111.png',
    alt: 'sky, карточка Ская.',
  },
  taya: {
    name: 'Тая',
    frame: 'assets/images/figma-2026/dog-frames/Тая.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 104.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 118.png',
    alt: 'taya, карточка Таи.',
  },
  elis: {
    name: 'Элис',
    frame: 'assets/images/figma-2026/dog-frames/Элис.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 102.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 116.png',
    alt: 'elis, карточка Элис.',
  },
  yasha: {
    name: 'Яша',
    frame: 'assets/images/figma-2026/dog-frames/Яша.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 101.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 115.png',
    alt: 'yasha, карточка Яши.',
  },
  iva: {
    name: 'Ива',
    frame: 'assets/images/figma-2026/dog-frames/Ива.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 128.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 142.png',
    alt: 'iva, карточка Ивы.',
  },
  lusya: {
    name: 'Люся',
    frame: 'assets/images/figma-2026/dog-frames/Люся.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 126.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 144.png',
    alt: 'lusya, карточка Люси.',
  },
  faya: {
    name: 'Фая',
    frame: 'assets/images/figma-2026/dog-frames/Марс-1.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 130.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 138.png',
    alt: 'faya, карточка Фаи.',
  },
  feya: {
    name: 'Фея',
    frame: 'assets/images/figma-2026/dog-frames/Фея.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 133.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 139.png',
    alt: 'feya, карточка Феи.',
  },
  fiona: {
    name: 'Фиона',
    frame: 'assets/images/figma-2026/dog-frames/Фиона.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 134.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 140.png',
    alt: 'fiona, карточка Фионы.',
  },
  vesi: {
    name: 'Веси',
    frame: 'assets/images/figma-2026/dog-frames/Веси.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 97.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 135.png',
    alt: 'vesi, карточка Веси.',
  },
  ryzhik: {
    name: 'Рыжик',
    frame: 'assets/images/figma-2026/dog-frames/Рыжик.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 127.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 137.png',
    alt: 'ryzhik, карточка Рыжика.',
  },
  mars: {
    name: 'Марс',
    frame: 'assets/images/figma-2026/dog-frames/Марс.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 129.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 136.png',
    alt: 'mars, карточка Марса.',
  },
  pups: {
    name: 'Пупс',
    frame: 'assets/images/figma-2026/dog-frames/Пупс.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 131.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 143.png',
    alt: 'pups, карточка Пупса.',
  },
  pirate: {
    name: 'Пират',
    frame: 'assets/images/figma-2026/dog-frames/Пират.png',
    cardDesktop: 'assets/images/figma-2026/dog-cards-desktop/Group 132.png',
    cardMobile: 'assets/images/figma-2026/dog-cards-mobile/Group 141.png',
    alt: 'pirate, карточка Пирата.',
  },
};

const dogOrder = [
  'klepa',
  'belka',
  'tolik',
  'persey',
  'alya',
  'johnny',
  'kesha',
  'maylo',
  'sky',
  'taya',
  'elis',
  'yasha',
  'iva',
  'lusya',
  'pirate',
  'faya',
  'feya',
  'fiona',
  'vesi',
  'ryzhik',
  'mars',
  'pups',
];

const brandCards = {
  plushki: {
    cardDesktop: 'assets/images/figma-2026/brand-cards/Group 105.png',
    cardMobile: 'assets/images/figma-2026/brand-cards-mobile/Group-123-plushki.png?v=20260527-brand-frames',
    alt: 'Карточка бренда Плюшки.',
    href: 'https://petvkus.ru',
  },
  sobakamama: {
    cardDesktop: 'assets/images/figma-2026/brand-cards/Group 96.png',
    cardMobile: 'assets/images/figma-2026/brand-cards-mobile/Group-124-sobakamama.png?v=20260527-brand-frames',
    alt: 'Карточка бренда Собака Мама.',
    href: 'https://sobakamama.shop',
  },
  sobakin: {
    cardDesktop: 'assets/images/figma-2026/brand-cards/Group 83.png',
    cardMobile: 'assets/images/figma-2026/brand-cards-mobile/Group-125-sobakin.png?v=20260527-brand-frames',
    alt: 'Карточка бренда Собакин.',
    href: 'https://sobakin-shop.ru',
  },
  'shaggy-dog': {
    cardDesktop: 'assets/images/figma-2026/brand-cards/Group 64.png',
    cardMobile: 'assets/images/figma-2026/brand-cards-mobile/Group-121-shaggy-dog.png?v=20260527-brand-frames',
    alt: 'Карточка бренда Shaggy Dog.',
    href: 'https://shaggydog.ru',
  },
  'derzhis-menya': {
    cardDesktop: 'assets/images/figma-2026/brand-cards/Group 67.png',
    cardMobile: 'assets/images/figma-2026/brand-cards-mobile/Group-122-derzhis-menya.png?v=20260527-brand-frames',
    alt: 'Карточка бренда Держись меня.',
    href: 'https://t.me/derzhismenya',
  },
  'hug-me-dog': {
    cardDesktop: 'assets/images/figma-2026/brand-cards/Group 63.png',
    cardMobile: 'assets/images/figma-2026/brand-cards-mobile/Group-120-hug-me-dog.png?v=20260527-brand-frames',
    alt: 'Карточка бренда Hug Me Dog.',
    href: 'https://hugmedog.ru',
  },
};

const eventSlides = [
  {
    src: 'assets/images/figma-2026/events/rbTVTeycB2U8paixWNAPHVwCGOsGAzZ0FAYRZ1dPS46CNMb_u1CqoSNGbIfHcfZBBo 1.png',
    alt: 'Стенд Mr.Kranch с игрушками и товарами для собак.',
  },
  {
    src: 'assets/images/figma-2026/events/unnamed (1) (1) 1.png',
    alt: 'Бокс Хвост Ньюс на фестивале.',
  },
  {
    src: 'assets/images/figma-2026/events/unnamed (2) (1) 1.png',
    alt: 'Товары и лакомства для собак на стенде партнеров.',
  },
];

const djCards = {
  maksim: {
    src: 'assets/images/figma-2026/djs/maksim-myself.png',
    alt: 'Карточка диджея Maksim Myself.',
    href: 'https://t.me/tochnodj',
  },
  stepan: {
    src: 'assets/images/figma-2026/djs/stepan-nepal.png',
    alt: 'Карточка диджея Stepan Nepal.',
    href: 'https://t.me/nepal_prod',
  },
};

const dogTrack = document.querySelector('[data-dog-track]');
const dogPager = document.querySelector('[data-dog-pager]');
const dogViewport = document.querySelector('.dog-carousel__viewport');

function renderDogCarousel() {
  if (!dogTrack) {
    return;
  }

  dogTrack.replaceChildren(...dogOrder.map((dogKey, index) => {
    const dog = dogCards[dogKey];
    const button = document.createElement('button');
    const image = document.createElement('img');

    button.className = 'dog-frame-button';
    button.type = 'button';
    button.dataset.dog = dogKey;
    button.setAttribute('aria-label', `Открыть карточку ${dog.name}`);

    image.loading = index === 0 ? 'eager' : 'lazy';
    image.decoding = 'async';
    image.fetchPriority = index === 0 ? 'high' : 'low';
    image.src = dog.frame;
    image.alt = dog.name;
    button.append(image);

    return button;
  }));
}

renderDogCarousel();

const modal = document.querySelector('.dog-modal');
const modalImage = document.querySelector('.dog-modal__image');
const brandLink = document.querySelector('[data-brand-link]');
const closeButton = document.querySelector('.dog-modal__close');
const infoModal = document.querySelector('.info-modal');
const infoText = document.querySelector('.info-modal__text');
const infoCloseButton = document.querySelector('.info-modal__close');
const dogButtons = [...document.querySelectorAll('[data-dog]')];
const dogPageButtons = [];
const brandButtons = [...document.querySelectorAll('[data-brand]')];
const djButtons = [...document.querySelectorAll('[data-dj]')];
const eventImage = document.querySelector('[data-event-carousel-image]');
const eventButtons = [...document.querySelectorAll('[data-event-carousel]')];
const dogStatus = document.querySelector('.dog-status');
const faqButtons = [...document.querySelectorAll('[data-faq]')];
const scrollTopButton = document.querySelector('.scroll-top');
let activeDogIndex = 0;
let activeDogPage = 0;
let activeEventIndex = 0;
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const mobileViewport = window.matchMedia('(max-width: 700px)');

function applyMobileHotspotTweaks() {
  const isMobile = mobileViewport.matches;

  document.querySelectorAll('.brand-card-hotspot').forEach((hotspot) => {
    hotspot.style.zIndex = isMobile ? '12' : '';
  });
}

applyMobileHotspotTweaks();

function dogPageSize() {
  return mobileViewport.matches ? 1 : 4;
}

function preloadCriticalImages() {
  const firstDog = dogCards[dogOrder[0]];
  if (!firstDog) {
    return;
  }

  const preload = (source) => {
    if (!source) {
      return;
    }
    const image = new Image();
    image.src = source;
  };

  preload(firstDog.frame);

  if (!mobileViewport.matches) {
    preload(firstDog.cardDesktop);
  }
}

function scheduleInitialPreload() {
  const run = () => {
    window.setTimeout(preloadCriticalImages, 220);
  };

  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(run, { timeout: 1200 });
    return;
  }

  run();
}

if (document.readyState === 'complete') {
  scheduleInitialPreload();
} else {
  window.addEventListener('load', scheduleInitialPreload, { once: true });
}

function updateDogTrack() {
  const activeButton = dogButtons[activeDogIndex];

  if (!dogTrack || !activeButton) {
    return;
  }

  const slide = activeButton.offsetLeft - dogButtons[0].offsetLeft;
  dogTrack.style.setProperty('--dog-slide', `${slide}px`);
}

function updateDogPager() {
  dogPageButtons.forEach((button, index) => {
    const isActive = index === activeDogPage;
    button.classList.toggle('is-active', isActive);
    button.setAttribute('aria-current', isActive ? 'true' : 'false');
  });
}

function setActiveDog(index, shouldAnnounce = true) {
  activeDogIndex = (index + dogOrder.length) % dogOrder.length;
  activeDogPage = Math.floor(activeDogIndex / dogPageSize());
  const activeDog = dogOrder[activeDogIndex];

  dogButtons.forEach((button) => {
    button.classList.toggle('is-active', button.dataset.dog === activeDog);
  });

  updateDogTrack();
  updateDogPager();

  if (dogStatus && shouldAnnounce) {
    dogStatus.textContent = `Выбрана: ${dogCards[activeDog].name}`;
    dogStatus.classList.add('is-visible');
    window.clearTimeout(setActiveDog.timeout);
    setActiveDog.timeout = window.setTimeout(() => {
      dogStatus.classList.remove('is-visible');
    }, 1400);
  }
}

function setDogPage(page, shouldAnnounce = true) {
  const lastPage = Math.ceil(dogOrder.length / dogPageSize()) - 1;
  activeDogPage = (page + lastPage + 1) % (lastPage + 1);
  setActiveDog(activeDogPage * dogPageSize(), shouldAnnounce);
}

function renderDogPager() {
  if (!dogPager) {
    return;
  }

  const pageSize = dogPageSize();
  const pageCount = Math.ceil(dogOrder.length / pageSize);
  dogPageButtons.length = 0;
  dogPager.replaceChildren(...Array.from({ length: pageCount }, (_, index) => {
    const button = document.createElement('button');
    button.className = 'dog-carousel__page';
    button.type = 'button';
    button.dataset.dogPage = String(index);
    button.setAttribute('aria-label', `Показать собак ${index * pageSize + 1}-${Math.min((index + 1) * pageSize, dogOrder.length)}`);
    button.addEventListener('click', () => setDogPage(index));
    dogPageButtons.push(button);
    return button;
  }));
}

function openImageCard(card, options = {}) {
  if (!card || !modal || !modalImage) {
    return Promise.resolve();
  }

  modalImage.src = card.src;
  modalImage.alt = card.alt;
  if (brandLink) {
    brandLink.classList.toggle('is-visible', Boolean(options.showBrandLink && card.href));
    if (card.href) {
      brandLink.setAttribute('href', card.href);
    }
  }
  modal.classList.toggle('dog-modal--brand', options.modalMode === 'brand');
  modal.classList.toggle('dog-modal--dj', options.modalMode === 'dj');
  modal.classList.remove('is-closing');
  return modalImage.decode().catch(() => {}).then(() => {
    modal.showModal();
  });
}

function openDogCard(dogKey) {
  const dog = dogCards[dogKey];
  if (!dog) {
    return Promise.resolve();
  }

  return openImageCard({
    src: mobileViewport.matches ? dog.cardMobile : dog.cardDesktop,
    alt: dog.alt,
  });
}

function openBrandCard(brandKey) {
  const brand = brandCards[brandKey];
  if (!brand) {
    return Promise.resolve();
  }

  return openImageCard({
    src: mobileViewport.matches ? brand.cardMobile : brand.cardDesktop,
    alt: brand.alt,
    href: brand.href,
  }, { showBrandLink: true, modalMode: 'brand' });
}

function openDjCard(djKey) {
  return openImageCard(djCards[djKey], { showBrandLink: true, modalMode: 'dj' });
}

function setActiveEventSlide(index) {
  if (!eventImage) {
    return;
  }

  activeEventIndex = (index + eventSlides.length) % eventSlides.length;
  const slide = eventSlides[activeEventIndex];
  eventImage.src = slide.src;
  eventImage.alt = slide.alt;
  eventImage.dataset.eventIndex = String(activeEventIndex);
}

function closeDialog(dialog) {
  if (!dialog?.open) {
    return;
  }

  if (prefersReducedMotion.matches) {
    dialog.close();
    return;
  }

  if (dialog.classList.contains('is-closing')) {
    return;
  }

  let didClose = false;
  const finish = () => {
    if (didClose) {
      return;
    }

    didClose = true;
    dialog.classList.remove('is-closing');
    dialog.close();
  };

  dialog.classList.add('is-closing');
  const fallback = window.setTimeout(finish, 260);
  dialog.addEventListener('animationend', () => {
    window.clearTimeout(fallback);
    finish();
  }, { once: true });
}

dogButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    await openDogCard(button.dataset.dog);
  });
});

brandButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    await openBrandCard(button.dataset.brand);
  });
});

djButtons.forEach((button) => {
  button.addEventListener('click', async () => {
    await openDjCard(button.dataset.dj);
  });
});

document.querySelectorAll('[data-carousel]').forEach((button) => {
  button.addEventListener('click', () => {
    const direction = button.dataset.carousel === 'next' ? 1 : -1;
    setDogPage(activeDogPage + direction);
  });
});

eventButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const direction = button.dataset.eventCarousel === 'next' ? 1 : -1;
    setActiveEventSlide(activeEventIndex + direction);
  });
});

if (dogViewport) {
  let touchStartX = 0;
  let touchStartY = 0;
  const swipeThreshold = 34;

  dogViewport.addEventListener('touchstart', (event) => {
    const [touch] = event.touches;
    if (!touch) {
      return;
    }
    touchStartX = touch.clientX;
    touchStartY = touch.clientY;
  }, { passive: true });

  dogViewport.addEventListener('touchend', (event) => {
    const [touch] = event.changedTouches;
    if (!touch) {
      return;
    }

    const deltaX = touch.clientX - touchStartX;
    const deltaY = touch.clientY - touchStartY;
    if (Math.abs(deltaX) < swipeThreshold || Math.abs(deltaX) <= Math.abs(deltaY)) {
      return;
    }

    setDogPage(activeDogPage + (deltaX < 0 ? 1 : -1));
  }, { passive: true });
}

document.querySelectorAll('[data-info]').forEach((button) => {
  button.addEventListener('click', () => {
    if (!infoModal || !infoText) {
      return;
    }

    infoText.textContent = button.dataset.info || '';
    infoModal.classList.remove('is-closing');
    infoModal.showModal();
  });
});

faqButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const item = button.closest('.faq-item');
    const isOpen = item?.classList.toggle('is-open') || false;
    button.setAttribute('aria-expanded', String(isOpen));
  });
});

document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener('click', (event) => {
    const target = document.querySelector(link.getAttribute('href'));

    if (!target) {
      return;
    }

    event.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

closeButton?.addEventListener('click', () => {
  closeDialog(modal);
});

infoCloseButton?.addEventListener('click', () => {
  closeDialog(infoModal);
});

modal?.addEventListener('click', (event) => {
  if (event.target === modal) {
    closeDialog(modal);
  }
});

infoModal?.addEventListener('click', (event) => {
  if (event.target === infoModal) {
    closeDialog(infoModal);
  }
});

modal?.addEventListener('cancel', (event) => {
  event.preventDefault();
  closeDialog(modal);
});

infoModal?.addEventListener('cancel', (event) => {
  event.preventDefault();
  closeDialog(infoModal);
});

function updateScrollTopButton() {
  scrollTopButton?.classList.toggle('is-visible', window.scrollY > 650);
}

scrollTopButton?.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: prefersReducedMotion.matches ? 'auto' : 'smooth',
  });
});

window.addEventListener('resize', () => {
  applyMobileHotspotTweaks();
  renderDogPager();
  setActiveDog(activeDogIndex, false);
});
window.addEventListener('scroll', updateScrollTopButton, { passive: true });
updateScrollTopButton();

renderDogPager();
setActiveDog(0, false);
setActiveEventSlide(0);
