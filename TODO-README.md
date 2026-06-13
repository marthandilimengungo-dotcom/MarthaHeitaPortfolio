# To-Do List Application

A modern, fully functional to-do list application with local storage functionality. Built with vanilla HTML, CSS, and JavaScript.

## Features

✨ **Core Functionality**
- ➕ Add new tasks easily
- ✅ Mark tasks as completed
- 🗑️ Delete individual tasks
- 💾 Persistent storage using browser's localStorage
- 🔄 Automatic data persistence on every change

🎯 **Filtering System**
- View all tasks
- View only active tasks
- View only completed tasks
- Quick filter button switching

📊 **Additional Features**
- Task counter display
- Clear all completed tasks button
- Empty state message
- Responsive design for mobile devices
- XSS protection with HTML escaping
- Smooth animations and transitions

## How to Use

1. **Open the Application**: Open `index.html` in your web browser
2. **Add a Task**: 
   - Type your task in the input field
   - Press Enter or click the "Add Task" button
3. **Complete a Task**: 
   - Click the checkbox next to a task to mark it as complete
4. **Delete a Task**: 
   - Click the "Delete" button on any task
5. **Filter Tasks**: 
   - Use the filter buttons to view All, Active, or Completed tasks
6. **Clear Completed**: 
   - Click "Clear Completed" to remove all finished tasks

## Technical Details

### Local Storage
- All tasks are automatically saved to browser's localStorage
- Data persists between browser sessions
- Storage key: `todoList_tasks`

### Task Structure
Each task contains:
- `id`: Unique timestamp-based identifier
- `text`: The task description
- `completed`: Boolean flag for completion status
- `createdAt`: Timestamp when task was created

### Architecture
- Object-oriented design using a `TodoApp` class
- Event-driven architecture
- Real-time rendering on state changes
- Automatic UI synchronization

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Security Features

- HTML escaping to prevent XSS attacks
- Safe DOM manipulation practices
- Input validation

## Customization

You can customize the appearance by modifying `styles.css`:
- Change the gradient colors in the `body` background
- Adjust button colors and styles
- Modify spacing and sizing
- Update font families and sizes

## Files

- `index.html` - HTML structure and markup
- `styles.css` - Styling and responsive design
- `script.js` - Application logic and local storage handling
- `TODO-README.md` - This documentation

## Future Enhancements

Potential features for expansion:
- Task categories/tags
- Priority levels
- Due dates
- Local backup/export functionality
- Dark mode toggle
- Task editing capability
- Recurring tasks
- Subtasks support

---

**Made with ❤️ by Martha Heita**