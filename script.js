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

Object.values(dogCards).forEach((dog) => {
  const image = new Image();
  image.src = dog.src;
});

document.querySelectorAll('[data-dog]').forEach((button) => {
  button.addEventListener('click', async () => {
    const dog = dogCards[button.dataset.dog];

    if (!dog || !modal || !modalImage) {
      return;
    }

    modalImage.src = dog.src;
    modalImage.alt = dog.alt;
    await modalImage.decode().catch(() => {});
    modal.showModal();
  });
});

document.querySelectorAll('[data-info]').forEach((button) => {
  button.addEventListener('click', () => {
    if (!infoModal || !infoText) {
      return;
    }

    infoText.textContent = button.dataset.info || '';
    infoModal.showModal();
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
  modal?.close();
});

infoCloseButton?.addEventListener('click', () => {
  infoModal?.close();
});

modal?.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.close();
  }
});

infoModal?.addEventListener('click', (event) => {
  if (event.target === infoModal) {
    infoModal.close();
  }
});
