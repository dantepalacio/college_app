// function roundNumbers() {
//     let numberElements = document.getElementsByTagName("span");
//     for (let i = 0; i < numberElements.length; i++) {
//         let numberStr = numberElements[i].innerHTML;
//         let number = parseFloat(numberStr);
//         if (!isNaN(number)) {
//             if (number % 1 !== 0) {
//                 let roundedNumber = number.toFixed(1);
//                 numberElements[i].innerHTML = roundedNumber;
//             }
//         }
//     }       
// }

// window.onload = function() {
//     roundNumbers(); // вызовем функцию, чтобы округлить числа при загрузке страницы
// };