const dogCards = {
  klepa: {
    name: 'Клёпа',
    frame: 'assets/images/figma-2026/dog-frames/Frame 6.png',
    src: 'assets/images/figma-2026/dog-cards/Group 70.png',
    alt: 'klepa, карточка Клёпы.',
  },
  belka: {
    name: 'Белка',
    frame: 'assets/images/figma-2026/dog-frames/Frame 7.png',
    src: 'assets/images/figma-2026/dog-cards/Group 65.png',
    alt: 'belka, карточка Белки.',
  },
  tolik: {
    name: 'Толик',
    frame: 'assets/images/figma-2026/dog-frames/Frame 8.png',
    src: 'assets/images/figma-2026/dog-cards/Group 69.png',
    alt: 'tolik, карточка Толика.',
  },
  persey: {
    name: 'Персей',
    frame: 'assets/images/figma-2026/dog-frames/Frame 9.png',
    src: 'assets/images/figma-2026/dog-cards/Group 82.png',
    alt: 'persey, карточка Персея.',
  },
  alya: {
    name: 'Аля',
    frame: 'assets/images/figma-2026/dog-frames/Аля.png',
    src: 'assets/images/figma-2026/dog-cards/Group 99.png',
    alt: 'alya, карточка Али.',
  },
  johnny: {
    name: 'Джонни',
    frame: 'assets/images/figma-2026/dog-frames/Джонни.png',
    src: 'assets/images/figma-2026/dog-cards/Group 98.png',
    alt: 'johnny, карточка Джонни.',
  },
  kesha: {
    name: 'Кеша',
    frame: 'assets/images/figma-2026/dog-frames/Кеша.png',
    src: 'assets/images/figma-2026/dog-cards/Group 103.png',
    alt: 'kesha, карточка Кеши.',
  },
  maylo: {
    name: 'Майло',
    frame: 'assets/images/figma-2026/dog-frames/Майло.png',
    src: 'assets/images/figma-2026/dog-cards/Group 100.png',
    alt: 'maylo, карточка Майло.',
  },
  sky: {
    name: 'Скай',
    frame: 'assets/images/figma-2026/dog-frames/Скай.png',
    src: 'assets/images/figma-2026/dog-cards/Group 97.png',
    alt: 'sky, карточка Ская.',
  },
  taya: {
    name: 'Тая',
    frame: 'assets/images/figma-2026/dog-frames/Тая.png',
    src: 'assets/images/figma-2026/dog-cards/Group 104.png',
    alt: 'taya, карточка Таи.',
  },
  elis: {
    name: 'Элис',
    frame: 'assets/images/figma-2026/dog-frames/Элис.png',
    src: 'assets/images/figma-2026/dog-cards/Group 102.png',
    alt: 'elis, карточка Элис.',
  },
  yasha: {
    name: 'Яша',
    frame: 'assets/images/figma-2026/dog-frames/Яша.png',
    src: 'assets/images/figma-2026/dog-cards/Group 101.png',
    alt: 'yasha, карточка Яши.',
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
];

const brandCards = {
  petvkus: {
    src: 'assets/images/figma-2026/brand-cards/Group 105.png',
    alt: 'Карточка бренда Petvkus.',
    href: 'https://petvkus.ru',
  },
  sobakamama: {
    src: 'assets/images/figma-2026/brand-cards/Group 96.png',
    alt: 'Карточка бренда Собака Мама.',
    href: 'https://sobakamama.shop',
  },
  sobakin: {
    src: 'assets/images/figma-2026/brand-cards/Group 83.png',
    alt: 'Карточка бренда Собакин.',
    href: 'https://sobakin-shop.ru',
  },
  'shaggy-dog': {
    src: 'assets/images/figma-2026/brand-cards/Group 64.png',
    alt: 'Карточка бренда Shaggy Dog.',
    href: 'https://shaggydog.ru',
  },
  'derzhis-menya': {
    src: 'assets/images/figma-2026/brand-cards/Group 67.png',
    alt: 'Карточка бренда Держись меня.',
    href: 'https://t.me/derzhismenya',
  },
  'hug-me-dog': {
    src: 'assets/images/figma-2026/brand-cards/Group 63.png',
    alt: 'Карточка бренда Hug Me Dog.',
    href: 'https://hugmedog.ru',
  },
};

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

function renderDogCarousel() {
  if (!dogTrack) {
    return;
  }

  dogTrack.replaceChildren(...dogOrder.map((dogKey) => {
    const dog = dogCards[dogKey];
    const button = document.createElement('button');
    const image = document.createElement('img');

    button.className = 'dog-frame-button';
    button.type = 'button';
    button.dataset.dog = dogKey;
    button.setAttribute('aria-label', `Открыть карточку ${dog.name}`);

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
const dogStatus = document.querySelector('.dog-status');
const faqButtons = [...document.querySelectorAll('[data-faq]')];
const scrollTopButton = document.querySelector('.scroll-top');
let activeDogIndex = 0;
let activeDogPage = 0;
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

Object.values({ ...dogCards, ...brandCards, ...djCards }).forEach((card) => {
  const image = new Image();
  image.src = card.src;
  if (card.frame) {
    const frame = new Image();
    frame.src = card.frame;
  }
});

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
  activeDogPage = Math.floor(activeDogIndex / 4);
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
  const lastPage = Math.ceil(dogOrder.length / 4) - 1;
  activeDogPage = (page + lastPage + 1) % (lastPage + 1);
  setActiveDog(activeDogPage * 4, shouldAnnounce);
}

function renderDogPager() {
  if (!dogPager) {
    return;
  }

  const pageCount = Math.ceil(dogOrder.length / 4);
  dogPageButtons.length = 0;
  dogPager.replaceChildren(...Array.from({ length: pageCount }, (_, index) => {
    const button = document.createElement('button');
    button.className = 'dog-carousel__page';
    button.type = 'button';
    button.dataset.dogPage = String(index);
    button.setAttribute('aria-label', `Показать собак ${index * 4 + 1}-${Math.min((index + 1) * 4, dogOrder.length)}`);
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
  return openImageCard(dogCards[dogKey]);
}

function openBrandCard(brandKey) {
  return openImageCard(brandCards[brandKey], { showBrandLink: true, modalMode: 'brand' });
}

function openDjCard(djKey) {
  return openImageCard(djCards[djKey], { showBrandLink: true, modalMode: 'dj' });
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

window.addEventListener('resize', updateDogTrack);
window.addEventListener('scroll', updateScrollTopButton, { passive: true });
updateScrollTopButton();

renderDogPager();
setActiveDog(0, false);
