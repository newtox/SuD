document.addEventListener("DOMContentLoaded", () => {
  let started = false;
  const introOverlay = document.getElementById("intro-overlay");
  const container = document.getElementById("slides-container");
  window.addEventListener("keydown", (event) => {
    if (!started) {
      started = true;
      if (introOverlay) {
        introOverlay.style.opacity = "0";
        setTimeout(() => {
          introOverlay.style.display = "none";
        }, 500);
      }
      document.body.tabIndex = 0;
      document.body.focus();
    }
  }, {
    once: true
  });
  window.addEventListener("keydown", (event) => {
    if (!started) return;
    const slideWidth = window.innerWidth;
    let currentIndex = Math.round(container.scrollLeft / slideWidth);
    let targetIndex = currentIndex;
    if (event.key === "ArrowRight" || event.keyCode === 39) {
      event.preventDefault();
      targetIndex = currentIndex + 1;
    } else if (event.key === "ArrowLeft" || event.keyCode === 37) {
      event.preventDefault();
      targetIndex = currentIndex - 1;
    } else {
      return;
    }
    const maxIndex = container.children.length - 1;
    if (targetIndex < 0) {
      targetIndex = 0;
    } else if (targetIndex > maxIndex) {
      targetIndex = maxIndex;
    }
    container.style.scrollBehavior = "auto";
    container.scrollTo({
      left: targetIndex * window.innerWidth
    });
    setTimeout(() => {
      container.style.scrollBehavior = "smooth";
    }, 50);
  });

  const canvas = document.getElementById("effectsCanvas");
  if (!canvas) {
    console.error("Canvas element with id 'effectsCanvas' not found.");
    return;
  }
  const ctx = canvas.getContext("2d");
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  class Particle {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 5 + 2;
      this.speedX = Math.random() * 1 - 0.5;
      this.speedY = Math.random() * 1 - 0.5;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
      if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
    }
    draw() {
      ctx.fillStyle = "rgba(255,255,255,0.8)";
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  let particlesArray = [];
  const particlesCount = 200;
  for (let i = 0; i < particlesCount; i++) {
    particlesArray.push(new Particle());
  }

  function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
      particlesArray[i].update();
      particlesArray[i].draw();
    }
    requestAnimationFrame(animateParticles);
  }
  animateParticles();

  window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
});