# Digital Clock - Multiple Time Zones

A beautiful, real-time digital clock application displaying current time in different time zones. Built with vanilla HTML, CSS, and JavaScript.

## Features

⏰ **Core Functionality**
- Real-time clock updates every second
- Display time in 40+ different time zones
- Support for both 12-hour and 24-hour formats
- Add/remove time zones dynamically
- Persistent storage of selected time zones
- UTC offset information for each time zone

🎨 **Display Features**
- Large, readable digital display
- Current date display with full formatting
- Hour, minute, second breakdown
- UTC offset calculation
- Local time zone detection
- Responsive grid layout
- Animated local clock with glowing effect

🛠️ **User Controls**
- 12/24-hour format toggle
- Dropdown selector for adding time zones
- Remove button for each time zone card
- Reset to default time zones
- Local time display (always visible)

## How to Use

1. **Open the Application**: Open `clock.html` in your web browser
2. **View Default Time Zones**: The app starts with 4 default time zones:
   - America/New_York
   - Europe/London
   - Asia/Tokyo
   - Australia/Sydney

3. **Add a Time Zone**:
   - Select a time zone from the dropdown
   - Click "Add" button or press Enter
   - The new time zone will appear in the grid

4. **Remove a Time Zone**:
   - Click the "Remove" button on any clock card

5. **Change Time Format**:
   - Uncheck the "12-Hour Format" checkbox for 24-hour display
   - Check it again to return to 12-hour format

6. **Reset to Default**:
   - Click "Reset to Default" to restore the original 4 time zones

7. **View Local Time**:
   - Scroll down to see your local time zone and current time

## Supported Time Zones (40+)

**North America**
- America/New_York, America/Chicago, America/Denver
- America/Los_Angeles, America/Anchorage, Pacific/Honolulu
- America/Toronto, America/Mexico_City

**Europe**
- Europe/London, Europe/Paris, Europe/Berlin, Europe/Madrid
- Europe/Rome, Europe/Amsterdam, Europe/Brussels, Europe/Vienna
- Europe/Prague, Europe/Moscow

**Middle East & Africa**
- Asia/Dubai, Africa/Cairo, Africa/Johannesburg, Africa/Lagos

**Asia**
- Asia/Kolkata, Asia/Bangkok, Asia/Hong_Kong, Asia/Shanghai
- Asia/Tokyo, Asia/Seoul, Asia/Singapore

**South America**
- America/Sao_Paulo, America/Buenos_Aires, America/Lima, America/Caracas

**Oceania**
- Australia/Sydney, Australia/Melbourne, Australia/Brisbane
- Pacific/Auckland, Pacific/Fiji

**UTC**
- Coordinated Universal Time (UTC)

## Technical Details

### Architecture
- Object-oriented design using `DigitalClock` class
- Real-time updates with `setInterval`
- Browser's `Intl` API for accurate time zone conversion
- Automatic local time zone detection
- Local storage for user preferences

### Time Zone Handling
- Uses native JavaScript `Intl.DateTimeFormat` for accuracy
- Automatic UTC offset calculation
- Proper handling of daylight saving time
- Cross-browser compatible

### Storage
- Stores selected time zones in browser's localStorage
- Key: `selectedTimezones`
- Automatic persistence across sessions
- Fallback to default time zones if storage fails

## Files

- `clock.html` - HTML structure and markup
- `clock-styles.css` - Comprehensive styling with animations
- `clock-script.js` - Application logic and time zone handling
- `CLOCK-README.md` - This documentation

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Customization

Modify `clock-styles.css` to customize:
- Background gradient colors
- Font sizes and styling
- Card colors and shadows
- Animation speeds
- Layout dimensions

Add more time zones by editing the `timezones` array in `clock-script.js`:
```javascript
this.timezones = [
    'Your/Timezone',
    'Another/Timezone',
    // ... more zones
];
```

Change default time zones:
```javascript
this.defaultTimezones = [
    'America/New_York',
    'Your/Default/Zone',
    // ... more zones
];
```

## Performance

- Optimized for real-time updates
- Single interval timer for all clocks
- Efficient DOM manipulation
- Minimal memory footprint
- Smooth animations without performance lag

## Future Enhancements

Potential features for expansion:
- World map with time zones
- Analog clock display
- Alarm functionality
- Stopwatch/timer
- Meeting time finder
- Time zone search
- Custom time zone groups
- Sound notifications
- Dark/light theme toggle
- Favorite time zones

---

**Made with ❤️ by Martha Heita**