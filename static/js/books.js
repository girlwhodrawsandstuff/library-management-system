function searchBook() {
  let input, filter, table, tr, index;
  input = document.getElementById("search-input");
  filter = input.value.toUpperCase();
  table = document.getElementById("books-table");
  tr = table.getElementsByTagName("tr");
  for (index = 0; index < tr.length; index++) {
    const bookTitle = tr[index].getElementsByClassName("book-title")[0];
    const bookAuthors = tr[index].getElementsByClassName("book-authors")[0];
    if (bookTitle || bookAuthors) {
      let titleTextValue = bookTitle.textContent || bookTitle.innerText;
      let authorsTextValue = bookAuthors.textContent || bookAuthors.innextText;
      if (titleTextValue.toUpperCase().indexOf(filter) > -1 || authorsTextValue.toUpperCase().indexOf(filter) > -1) {
        tr[index].style.display = "";
      } else {
        tr[index].style.display = "none";
      }
    }
  }
}
