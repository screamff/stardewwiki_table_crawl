
let coll = document.getElementsByClassName("collapsible");
let i;
for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        let packagesContainer = this.parentElement.nextElementSibling;
        let isVisible = packagesContainer.style.display === 'flex';
        packagesContainer.style.display = isVisible ? 'none' : 'flex';
    });
}

function togglePackage(header) {
    let packageElement = header.nextElementSibling;
    let isVisible = packageElement.style.display === 'block';
    packageElement.style.display = isVisible ? 'none' : 'block';
}

function toggleItem(checkbox) {
    let itemElement = checkbox.parentElement;
    let packageElement = itemElement.parentElement.parentElement;

    if (checkbox.checked) {
        itemElement.classList.add('completed');
    } else {
        itemElement.classList.remove('completed');
    }

    let requiredCount = parseInt(packageElement.getAttribute('data-required'));
    let completedCount = packageElement.querySelectorAll('.item.completed').length;
    let num_element = packageElement.querySelector('span');
    num_element.innerHTML = completedCount;
    let h3 = packageElement.querySelector('h3');
    if (completedCount >= requiredCount) {
        h3.classList.add('bundlecompleted');
    } else {
        h3.classList.remove('bundlecompleted');
    }
}

function toggleAllCompleted() {
    let completedItems = document.querySelectorAll('.item.completed');
    let all_dis = true
    completedItems.forEach(item => {
        if (item.style.display == 'none') {
            all_dis = false
        }
    });
    if (all_dis) {
        completedItems.forEach(item => {
            item.style.display = 'none'
        });
    }
    else {
        completedItems.forEach(item => {
            item.style.display = 'flex'
        });
    }
}
