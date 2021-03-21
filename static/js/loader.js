var myVar;

function loader() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById(newFunction()).style.display = "block";

    function newFunction() {
        return "products";
    }
}
