const dogCards = {
  belka: {
    src: 'assets/images/figma-final/dog-belka.png',
    alt: 'Карточка Белки: 3 года, 10 кг, описание характера и ссылка на подробности.',
  },
  tolik: {
    src: 'assets/images/figma-final/dog-tolik.png',
    alt: 'Карточка Толика: 3 года, 12 кг, описание характера и ссылка на подробности.',
  },
  klepa: {
    src: 'assets/images/figma-final/dog-klepa.png',
    alt: 'Карточка Клепы: 4 года, 14 кг, описание характера и ссылка на подробности.',
  },
  persey: {
    src: 'assets/images/figma-final/dog-persey.png',
    alt: 'Карточка Персея: 2 года, 10 кг, описание характера и ссылка на подробности.',
  },
};

const modal = document.querySelector('.dog-modal');
const modalImage = document.querySelector('.dog-modal__image');
const closeButton = document.querySelector('.dog-modal__close');
const infoModal = document.querySelector('.info-modal');
const infoText = document.querySelector('.info-modal__text');
const infoCloseButton = document.querySelector('.info-modal__close');
const dogButtons = [...document.querySelectorAll('[data-dog]')];
const dogStatus = document.querySelector('.dog-status');
const faqButtons = [...document.querySelectorAll('[data-faq]')];
const dogOrder = ['klepa', 'belka', 'tolik', 'persey'];
const dogNames = {
  klepa: 'Клепа',
  belka: 'Белка',
  tolik: 'Толик',
  persey: 'Персей',
};
let activeDogIndex = 0;
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

Object.values(dogCards).forEach((dog) => {
  const image = new Image();
  image.src = dog.src;
});

function setActiveDog(index, shouldAnnounce = true) {
  activeDogIndex = (index + dogOrder.length) % dogOrder.length;
  const activeDog = dogOrder[activeDogIndex];

  dogButtons.forEach((button) => {
    button.classList.toggle('is-active', button.dataset.dog === activeDog);
  });

  if (dogStatus && shouldAnnounce) {
    dogStatus.textContent = `Выбрана: ${dogNames[activeDog]}`;
    dogStatus.classList.add('is-visible');
    window.clearTimeout(setActiveDog.timeout);
    setActiveDog.timeout = window.setTimeout(() => {
      dogStatus.classList.remove('is-visible');
    }, 1400);
  }
}

function openDogCard(dogKey) {
  const dog = dogCards[dogKey];

  if (!dog || !modal || !modalImage) {
    return Promise.resolve();
  }

  modalImage.src = dog.src;
  modalImage.alt = dog.alt;
  modal.classList.remove('is-closing');
  return modalImage.decode().catch(() => {}).then(() => {
    modal.showModal();
  });
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
    const dogIndex = dogOrder.indexOf(button.dataset.dog);
    setActiveDog(dogIndex, false);
    await openDogCard(button.dataset.dog);
  });
});

document.querySelectorAll('[data-carousel]').forEach((button) => {
  button.addEventListener('click', () => {
    const direction = button.dataset.carousel === 'next' ? 1 : -1;
    setActiveDog(activeDogIndex + direction);
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

setActiveDog(0, false);
