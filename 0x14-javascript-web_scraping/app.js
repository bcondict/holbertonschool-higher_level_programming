import 'regenerator-runtime/runtime';
import axios from 'axios';

// ...

const BASE_URL = 'https://jsonplaceholder.typicode.com';

const getTodoItems = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/todos?_limit=5`);

    const todoItems = response.data;

    console.log('GET: Here\'s the list of todos', todoItems);

    return todoItems;
  } catch (errors) {
    console.error(errors);
  }
};
// ...

const createTodoElement = item => {
  const todoElement = document.createElement('li');

  todoElement.appendChild(document.createTextNode(item.title));

  return todoElement;
};

const updateTodoList = todoItems => {
  const todoList = document.querySelector('ul');

  if (Array.isArray(todoItems) && todoItems.length > 0) {
    todoItems.map(todoItem => {
      todoList.appendChild(createTodoElement(todoItem));
    });
  } else if (todoItems) {
    todoList.appendChild(createTodoElement(todoItems));
  }
};

const main = async () => {
  updateTodoList(await getTodoItems());
};

main();
// ...

const form = document.querySelector('form');

form.addEventListener('submit', async event => {
  event.preventDefault();

  const title = document.querySelector('#new-todos__title').value;

  const todo = {
    userId: 1,
    title: title,
    completed: false
  };

  const submitTodoItem = await addTodoItem(todo);
  updateTodoList(submitTodoItem);
});
// ...

export const addTodoItem = async todo => {
  try {
    const response = await axios.post(`${BASE_URL}/todos`, todo);
    const newTodoItem = response.data;

    console.log('Added a new Todo!', newTodoItem);

    return newTodoItem;
  } catch (errors) {
    console.error(errors);
  }
};
// ...

export const deleteTodoItem = async id => {
  try {
    const response = await axios.delete(`${BASE_URL}/todos/${id}`);
    console.log('Deleted Todo ID: ', id);

    return response.data;
  } catch (errors) {
    console.error(errors);
  }
};
// ...

const removeTodoElement = async (event, element) => {
  event.target.parentElement.removeChild(element);
  const id = element.id;

  await deleteTodoItem(id);
};
  <div id='new-todos'>
    <h1>New Todo</h1>
    <form>
      <label>
        Name
        <input type='text' id='new-todos__title' />
      </label>
      <button type='submit'>Add</button>
    </form>
  </div>;
