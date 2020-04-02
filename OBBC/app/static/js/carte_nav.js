/* Script pour la carte intéractive */

// on crée les différentes variables :

var map = document.querySelector('#map'); // variable qui contient la carte (map)

var paths = map.querySelectorAll('.map__image a');    //variable qui selectionne les différents chemins de formes géométriques (paths)

var links = map.querySelectorAll('.map__list a');   //variable qui selectionne les différents liens

// ajouts des événements

// Polyfill du foreach pour rendre for each compatible avec n'importe quel navigateur web (émulation)


if (NodeList.prototype.forEach === undefined){
    NodeList.prototype.forEach = function (callback) {
        [].forEach.call(this, callback)
    }
}

//fonction activeArea qui permet de lier les zones de la carte et les liens

var activeArea = function(id){
    map.querySelectorAll('.is-active').forEach(function (item) {
        
        item.classList.remove('is-active')
        
    })
    
    if (id !== undefined){

        document.querySelector('#list-' + id).classList.add('is-active')
        document.querySelector('#region-' + id).classList.add('is-active')

    }
    
}


// event : passage sur les zones de la carte

paths.forEach(function (path) {
    path.addEventListener('mouseenter', function () {

        var id = this.id.replace('region-','')

        activeArea(id)

    })

})


// event : passage sur les liens

links.forEach(function (link) {

    link.addEventListener('mouseenter', function () {

        var id = this.id.replace('list-','')

        activeArea(id)

    })

})

// event : lorsque l'on quitte la zone de la carte, les régions de dialectes sont déselectionées

map.addEventListener('mouseleave', function () {

    activeArea()
    
})

// event : lorsque l'on quitte la zone des liens, les liens sont déselectionées

links.addEventListener('mouseleave', function () {

    activeArea()

})