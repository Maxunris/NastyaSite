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
const faqPanel = document.querySelector('.faq-panel');
const faqButtons = [...document.querySelectorAll('[data-faq]')];
const dogOrder = ['klepa', 'belka', 'tolik', 'persey'];
const dogNames = {
  klepa: 'Клепа',
  belka: 'Белка',
  tolik: 'Толик',
  persey: 'Персей',
};
const faqAnswers = [
  'Конечно! Наш фестиваль семейное событие, где будет интересно и взрослым, и детям.',
  'Да, вы можете прийти со своим питомцем, если он социализирован и не агрессивен к другим собакам и людям.',
  'Паспорт и небольшой рассказ о себе. Если вы забираете питомца, понадобится написать заявление.',
  'Да. В программе лекции от профессиональных кинологов, ветеринаров и зоопсихологов.',
  'Можно стать волонтером, сделать пожертвование или купить приятные и полезные вещи на маркете.',
  'Отлично! Присылайте вопросы и предложения в Telegram: @anastasia_sabanina.',
];
let activeDogIndex = 0;
let openFaqIndex = null;

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
  return modalImage.decode().catch(() => {}).then(() => {
    modal.showModal();
  });
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
    infoModal.showModal();
  });
});

faqButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const index = Number(button.dataset.faq);
    const isOpen = openFaqIndex === index;

    faqButtons.forEach((faqButton) => {
      faqButton.classList.remove('is-open');
      faqButton.setAttribute('aria-expanded', 'false');
    });

    if (!faqPanel || isOpen) {
      openFaqIndex = null;
      faqPanel?.classList.remove('is-open');
      return;
    }

    const top = button.offsetTop + button.offsetHeight + 6;
    openFaqIndex = index;
    button.classList.add('is-open');
    button.setAttribute('aria-expanded', 'true');
    faqPanel.textContent = faqAnswers[index] || '';
    faqPanel.style.top = `${top}px`;
    faqPanel.classList.add('is-open');
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

setActiveDog(0, false);
