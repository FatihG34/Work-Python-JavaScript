//* In here,  callback has been practiced
// const todos = [
//     { title: "todo 1", description: "work asyncron programing" },
//     { title: "todo 2", description: "work API" },
//     { title: "todo 3", description: "work OOP" },
// ];

// let todoListEl = document.querySelector("#todoList");


// function todoList() {
//     setTimeout(() => {
//         todoItems = "";
//         todos.forEach(item => {
//             todoItems += `
//     <li>
//     <b>${item.title}</b>
//     <p>${item.description}</p>
//     </li>`
//         })
//         todoListEl.innerHTML = todoItems;
//     }, 1000);
// };

// function newTodo(todo, callMe) {
//     setTimeout(() => {
//         todos.push(todo);
//         callMe();
//     }, 1500);
// };

// newTodo({
//     title: "todo 4",
//     description: "kendine vakit ayır..."
// }, todoList);

// todoList();
//!  Asyncron primise practiced

const todos = [
    { title: "todo 1", description: "work asyncron programing" },
    { title: "todo 2", description: "work API" },
    { title: "todo 3", description: "work OOP" },
];

let todoListEl = document.querySelector("#todoList");


// function todoList() {
//     setTimeout(() => {
//         todoItems = "";
//         todos.forEach(item => {
//             todoItems += `<li>
//                             <b>${item.title}</b>
//                             <p>${item.description}</p>
//                           </li>`
//         });
//         todoListEl.innerHTML = todoItems;
//     }, 1000);
// };
// function newTodo(todo) {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             todos.push(todo);
//             const err = false;
//             if (!err) {
//                 resolve(todos);
//             } else {
//                 reject("Have an Error!!!...");
//             }
//         }, 1500);
//     })

// };
// newTodo({
//     title: "todo 4",
//     description: "kendine vakit ayır..."
// }).then((response) => {
//     console.log("New Array :", response);
//     todoList();
// }).catch((e) => {
//     console.log(e);
// })

// todoList();



//* async-await practice

async function fetchPost() {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts`);
    const data = await response.json();
    console.log(data);
    data.forEach(i => {
        console.log("i", i);
    });
};
fetchPost();

const ulkeler = async () => {
    const ulkeList = await fetch("https://jsonplaceholder.typicode.com/posts");
    const ulke = await ulkeList.json();
    console.log(ulke[0]);
};

ulkeler();