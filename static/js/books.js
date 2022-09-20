const modal = document.getElementById("modal");
const openModalButton = document.getElementById("open-modal");
const closeModalButton = document.getElementById("close-modal");

openModalButton.addEventListener('click', () => {
    modal.classList.add("show-modal");
});

closeModalButton.addEventListener('click', () => {
    modal.classList.remove("show-modal");
});