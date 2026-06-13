// To-Do List Application with Local Storage

class TodoApp {
    constructor() {
        this.todos = [];
        this.currentFilter = 'all';
        this.storageKey = 'todoList_tasks';
        
        // DOM Elements
        this.todoInput = document.getElementById('todoInput');
        this.addBtn = document.getElementById('addBtn');
        this.todoList = document.getElementById('todoList');
        this.totalTasks = document.getElementById('totalTasks');
        this.clearCompleted = document.getElementById('clearCompleted');
        this.filterBtns = document.querySelectorAll('.filter-btn');
        
        this.init();
    }
    
    init() {
        this.loadFromStorage();
        this.setupEventListeners();
        this.render();
    }
    
    setupEventListeners() {
        // Add task
        this.addBtn.addEventListener('click', () => this.addTodo());
        this.todoInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.addTodo();
        });
        
        // Filter buttons
        this.filterBtns.forEach(btn => {
            btn.addEventListener('click', () => this.setFilter(btn.dataset.filter));
        });
        
        // Clear completed
        this.clearCompleted.addEventListener('click', () => this.removeCompleted());
    }
    
    addTodo() {
        const text = this.todoInput.value.trim();
        
        if (text === '') {
            alert('Please enter a task!');
            return;
        }
        
        const todo = {
            id: Date.now(),
            text: text,
            completed: false,
            createdAt: new Date().toLocaleString()
        };
        
        this.todos.unshift(todo);
        this.todoInput.value = '';
        this.saveToStorage();
        this.render();
        this.todoInput.focus();
    }
    
    deleteTodo(id) {
        this.todos = this.todos.filter(todo => todo.id !== id);
        this.saveToStorage();
        this.render();
    }
    
    toggleComplete(id) {
        const todo = this.todos.find(todo => todo.id === id);
        if (todo) {
            todo.completed = !todo.completed;
            this.saveToStorage();
            this.render();
        }
    }
    
    setFilter(filter) {
        this.currentFilter = filter;
        
        // Update active button
        this.filterBtns.forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.filter === filter) {
                btn.classList.add('active');
            }
        });
        
        this.render();
    }
    
    removeCompleted() {
        this.todos = this.todos.filter(todo => !todo.completed);
        this.saveToStorage();
        this.render();
    }
    
    getFilteredTodos() {
        switch(this.currentFilter) {
            case 'active':
                return this.todos.filter(todo => !todo.completed);
            case 'completed':
                return this.todos.filter(todo => todo.completed);
            default:
                return this.todos;
        }
    }
    
    render() {
        const filteredTodos = this.getFilteredTodos();
        this.todoList.innerHTML = '';
        
        if (filteredTodos.length === 0) {
            this.todoList.innerHTML = `
                <div class="empty-state">
                    <p>📭 No tasks to display</p>
                </div>
            `;
        } else {
            filteredTodos.forEach(todo => {
                const li = document.createElement('li');
                li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
                li.innerHTML = `
                    <input 
                        type="checkbox" 
                        class="todo-checkbox" 
                        ${todo.completed ? 'checked' : ''}
                        data-id="${todo.id}"
                    >
                    <span class="todo-text">${this.escapeHtml(todo.text)}</span>
                    <button class="delete-btn" data-id="${todo.id}">Delete</button>
                `;
                
                // Add event listeners
                li.querySelector('.todo-checkbox').addEventListener('change', () => {
                    this.toggleComplete(todo.id);
                });
                
                li.querySelector('.delete-btn').addEventListener('click', () => {
                    this.deleteTodo(todo.id);
                });
                
                this.todoList.appendChild(li);
            });
        }
        
        this.updateStats();
    }
    
    updateStats() {
        const totalCount = this.todos.length;
        const completedCount = this.todos.filter(todo => todo.completed).length;
        const activeCount = totalCount - completedCount;
        
        const taskText = totalCount === 1 ? 'task' : 'tasks';
        this.totalTasks.textContent = `${totalCount} ${taskText}`;
        
        // Show/hide clear button
        this.clearCompleted.style.display = completedCount > 0 ? 'block' : 'none';
    }
    
    saveToStorage() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.todos));
    }
    
    loadFromStorage() {
        const stored = localStorage.getItem(this.storageKey);
        if (stored) {
            try {
                this.todos = JSON.parse(stored);
            } catch (error) {
                console.error('Error loading todos from storage:', error);
                this.todos = [];
            }
        }
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new TodoApp();
});