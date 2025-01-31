const coll = document.getElementsByClassName("collapsible");
const itens = document.getElementsByClassName('item');
const contents = document.getElementsByClassName('content');

for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        //this.classList.toggle("active");
        let content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

for (let i = 0; i < itens.length; i++) {
    itens[i].addEventListener('click', function () {
        for (item of itens) {
            item.classList.remove("active");
        }
        this.classList.toggle("active");
        for (let j = 0; j<contents.length;j++){
            if (i !== j) {
                let content = contents[j];
                content.style.display = "none";
            }
        }
        let content = contents[i];
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}
//Roadmap
//For Data Science
//A ideia aqui é apenas ter um roadmap de skills e projetos
//E treinar algumas coisas básicas de JS
