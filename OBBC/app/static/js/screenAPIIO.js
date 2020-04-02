/* script pour l'apparition au défillement - Intersection Observer API-https://developer.mozilla.org/fr/docs/Web/API/Intersection_Observer_API#Compatibilité_des_navigateurs */

const ratio = 0.34

const options = {
  root: null,
  rootMargin: '0px',
  threshold: ratio
}


const handleIntersect = function(entries, observer){
    entries.forEach(function (entry) {
        if (entry.intersectionRatio > ratio) {
            entry.target.classList.add('reveal-visible')
            observer.unobserve(entry.target)
        }
        console.log(entry.intersectionRatio)
    })
}


const observer = new IntersectionObserver(handleIntersect, options)
document.querySelectorAll('.reveal').forEach(function(r){
    observer.observe(r)
})
