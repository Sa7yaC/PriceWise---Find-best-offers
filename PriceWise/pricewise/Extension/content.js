document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.getElementById('searchForm');
  const linkInput = document.getElementById('linkInput');
  const productNameElement = document.getElementById('productName');
  const productImageElement = document.getElementById('productImage');

  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const url = linkInput.value.trim();
    if (url !== '') {
      fetch(`http://your-django-backend.com/getLink?text=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
          productNameElement.innerText = data.productName;
          productImageElement.src = data.productImage;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  });
});
