// Array para armazenar os itens do carrinho
let cart = [];

// Função para calcular o total do carrinho
function calculateCartTotal() {
  return cart.reduce((total, item) => total + parseFloat(item.price), 0).toFixed(2);
}

// Função para atualizar o conteúdo do modal do carrinho
function updateCartModal() {
  const cartItemsContainer = document.getElementById("cart-items");
  const totalContainer = document.getElementById("cart-total");
  
  cartItemsContainer.innerHTML = ""; // Limpar o conteúdo anterior

  if (cart.length === 0) {
    cartItemsContainer.innerHTML = "<p>O carrinho está vazio.</p>";
    totalContainer.innerHTML = "Total: R$ 0,00";
  } else {
    cart.forEach((item, index) => {
      const cartItem = `
        <div class="cart-item d-flex justify-content-between align-items-center mb-2">
          <img src="${item.img}" alt="${item.name}" width="50" height="50">
          <span>${item.name} - R$ ${item.price}</span>
          <button class="btn btn-danger btn-sm remove-from-cart" data-index="${index}">Remover</button>
        </div>
      `;
      cartItemsContainer.innerHTML += cartItem;
    });

    // Atualiza o total do carrinho
    totalContainer.innerHTML = `Total: R$ ${calculateCartTotal()}`;
  }
}

// Adicionar item ao carrinho
document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', (event) => {
    const name = button.getAttribute('data-name');
    const price = button.getAttribute('data-price');
    const img = button.getAttribute('data-img');

    // Adicionar o item ao array do carrinho
    cart.push({ name, price, img });

    // Atualizar o modal do carrinho
    updateCartModal();
  });
});

// Remover item do carrinho
document.addEventListener('click', (event) => {
  if (event.target.classList.contains('remove-from-cart')) {
    const index = event.target.getAttribute('data-index');
    cart.splice(index, 1); // Remover o item do array

    // Atualizar o modal do carrinho
    updateCartModal();
  }
});

// Limpar carrinho
document.getElementById('clear-cart').addEventListener('click', () => {
  cart = []; // Esvaziar o carrinho
  updateCartModal(); // Atualizar o modal do carrinho
});

