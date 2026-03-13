function openTab(x) {
    const y = parseInt(x);
    const content = document.querySelectorAll(".tache");
    const tabs = document.querySelectorAll(".onglets");

    // Masquer tout
    for (let i = 0; i < content.length; i++) {
        content[i].style.display = "none";
        tabs[i].classList.remove("active");
    }

    // Afficher celui qu'on veut
    if (content[y]) {
        content[y].style.display = "block";
        tabs[y].classList.add("active");
    }
}


function openClick(x) {
    const y = parseInt(x);
    const content = document.querySelectorAll(".ajouter");
    const tabs = document.querySelectorAll(".add");

    // Masquer tout
    for (let i = 0; i < content.length; i++) {
        content[i].style.display = "none";
        tabs[i].classList.remove("active");
    }

    // Afficher celui qu'on veut
    if (content[y]) {
        content[y].style.display = "block";
        tabs[y].classList.add("active");
    }
}
