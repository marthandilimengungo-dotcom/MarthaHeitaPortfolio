// Digital Clock with Multiple Time Zones

class DigitalClock {
    constructor() {
        this.selectedTimezones = [];
        this.is12Hour = true;
        this.storageKey = 'selectedTimezones';
        this.updateInterval = null;
        
        // All available time zones
        this.timezones = [
            'America/New_York',
            'America/Chicago',
            'America/Denver',
            'America/Los_Angeles',
            'America/Anchorage',
            'Pacific/Honolulu',
            'UTC',
            'Europe/London',
            'Europe/Paris',
            'Europe/Berlin',
            'Europe/Madrid',
            'Europe/Rome',
            'Europe/Amsterdam',
            'Europe/Brussels',
            'Europe/Vienna',
            'Europe/Prague',
            'Europe/Moscow',
            'Asia/Dubai',
            'Asia/Kolkata',
            'Asia/Bangkok',
            'Asia/Hong_Kong',
            'Asia/Shanghai',
            'Asia/Tokyo',
            'Asia/Seoul',
            'Asia/Singapore',
            'Australia/Sydney',
            'Australia/Melbourne',
            'Australia/Brisbane',
            'Pacific/Auckland',
            'Pacific/Fiji',
            'Africa/Cairo',
            'Africa/Johannesburg',
            'Africa/Lagos',
            'America/Toronto',
            'America/Mexico_City',
            'America/Sao_Paulo',
            'America/Buenos_Aires',
            'America/Lima',
            'America/Caracas'
        ];
        
        this.defaultTimezones = [
            'America/New_York',
            'Europe/London',
            'Asia/Tokyo',
            'Australia/Sydney'
        ];
        
        this.init();
    }
    
    init() {
        this.setupDOM();
        this.setupEventListeners();
        this.loadFromStorage();
        this.populateTimezoneDropdown();
        this.startClock();
    }
    
    setupDOM() {
        this.clocksContainer = document.getElementById('clocksContainer');
        this.formatToggle = document.getElementById('formatToggle');
        this.addTimezoneSelect = document.getElementById('addTimezone');
        this.addBtn = document.getElementById('addBtn');
        this.resetBtn = document.getElementById('resetBtn');
        this.localClock = document.getElementById('localClock');
        this.localDate = document.getElementById('localDate');
        this.localTimezone = document.getElementById('localTimezone');
    }
    
    setupEventListeners() {
        this.formatToggle.addEventListener('change', (e) => {
            this.is12Hour = e.target.checked;
            this.updateAllClocks();
        });
        
        this.addBtn.addEventListener('click', () => this.addTimezone());
        this.resetBtn.addEventListener('click', () => this.resetToDefault());
        
        this.addTimezoneSelect.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.addTimezone();
        });
    }
    
    populateTimezoneDropdown() {
        this.addTimezoneSelect.innerHTML = '<option value="">-- Select a time zone --<\/option>';
        
        this.timezones.forEach(tz => {
            if (!this.selectedTimezones.includes(tz)) {
                const option = document.createElement('option');
                option.value = tz;
                option.textContent = this.formatTimezoneName(tz);
                this.addTimezoneSelect.appendChild(option);
            }
        });
    }
    
    addTimezone() {
        const timezone = this.addTimezoneSelect.value;
        
        if (!timezone) {
            alert('Please select a time zone');
            return;
        }
        
        if (this.selectedTimezones.includes(timezone)) {
            alert('This time zone is already added');
            return;
        }
        
        this.selectedTimezones.push(timezone);
        this.saveToStorage();
        this.render();
        this.populateTimezoneDropdown();
        this.addTimezoneSelect.value = '';
    }
    
    removeTimezone(timezone) {
        this.selectedTimezones = this.selectedTimezones.filter(tz => tz !== timezone);
        this.saveToStorage();
        this.render();
        this.populateTimezoneDropdown();
    }
    
    resetToDefault() {
        if (confirm('Are you sure you want to reset to default time zones?')) {
            this.selectedTimezones = [...this.defaultTimezones];
            this.saveToStorage();
            this.render();
            this.populateTimezoneDropdown();
        }
    }
    
    startClock() {
        this.updateAllClocks();
        this.updateInterval = setInterval(() => this.updateAllClocks(), 1000);
    }
    
    updateAllClocks() {
        this.updateLocalClock();
        this.render();
    }
    
    updateLocalClock() {
        const now = new Date();
        const timeStr = this.formatTime(now, 'UTC');
        const localTz = Intl.DateTimeFormat().resolvedOptions().timeZone;
        
        this.localClock.textContent = this.formatTime(now, 'UTC', true);
        this.localDate.textContent = this.formatDate(now);
        this.localTimezone.textContent = this.formatTimezoneName(localTz);
    }
    
    render() {
        this.clocksContainer.innerHTML = '';
        
        if (this.selectedTimezones.length === 0) {
            this.clocksContainer.innerHTML = '<div class="empty-state">No time zones selected. Add one to get started!</div>';
            return;
        }
        
        this.selectedTimezones.forEach(timezone => {
            const clockCard = this.createClockCard(timezone);
            this.clocksContainer.appendChild(clockCard);
        });
    }
    
    createClockCard(timezone) {
        const now = new Date();
        const formatter = new Intl.DateTimeFormat('en-US', {
            timeZone: timezone,
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
        
        const parts = formatter.formatToParts(now);
        const getPartValue = (partType) => parts.find(p => p.type === partType)?.value;
        
        let hours = parseInt(getPartValue('hour'));
        const minutes = getPartValue('minute');
        const seconds = getPartValue('second');
        
        let timeStr;
        if (this.is12Hour) {
            const ampm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12;
            hours = hours ? hours : 12;
            timeStr = `${String(hours).padStart(2, '0')}:${minutes}:${seconds}`;
        } else {
            timeStr = `${String(hours).padStart(2, '0')}:${minutes}:${seconds}`;
        }
        
        const day = getPartValue('day');
        const month = getPartValue('month');
        const year = getPartValue('year');
        const dateStr = `${month}/${day}/${year}`;
        
        const card = document.createElement('div');
        card.className = 'clock-card';
        card.innerHTML = `
            <div class="timezone-name">${this.formatTimezoneName(timezone)}</div>
            <div class="digital-display">${timeStr}</div>
            <div class="date-display">${dateStr}</div>
            <div class="time-details">
                <div class="detail-item">
                    <span class="detail-label">Hour:</span>
                    <span>${String(hours).padStart(2, '0')}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Minute:</span>
                    <span>${minutes}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">Second:</span>
                    <span>${seconds}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">UTC Offset:</span>
                    <span>${this.getUTCOffset(timezone)}</span>
                </div>
            </div>
            <button class="remove-btn" data-timezone="${timezone}">Remove</button>
        `;
        
        card.querySelector('.remove-btn').addEventListener('click', () => {
            this.removeTimezone(timezone);
        });
        
        return card;
    }
    
    formatTime(date, timezone = 'UTC', useLocalFormat = false) {
        const formatter = new Intl.DateTimeFormat('en-US', {
            timeZone: timezone,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
        
        return formatter.format(date);
    }
    
    formatDate(date) {
        const formatter = new Intl.DateTimeFormat('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
        
        return formatter.format(date);
    }
    
    formatTimezoneName(tz) {
        return tz.replace(/_/g, ' ').split('/').pop();
    }
    
    getUTCOffset(timezone) {
        const now = new Date();
        const formatter = new Intl.DateTimeFormat('en-CA', {
            timeZone: timezone,
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
        
        const tzTime = new Date(formatter.format(now).replace(/(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/, '$1/$2/$3 $4:$5:$6'));
        const utcTime = new Date(now.toLocaleString('en-US', { timeZone: 'UTC' }));
        
        const offset = Math.round((tzTime - now) / (1000 * 60 * 60));
        const sign = offset >= 0 ? '+' : '';
        
        return `UTC ${sign}${offset}`;
    }
    
    saveToStorage() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.selectedTimezones));
    }
    
    loadFromStorage() {
        const stored = localStorage.getItem(this.storageKey);
        if (stored) {
            try {
                this.selectedTimezones = JSON.parse(stored);
            } catch (error) {
                console.error('Error loading from storage:', error);
                this.selectedTimezones = [...this.defaultTimezones];
            }
        } else {
            this.selectedTimezones = [...this.defaultTimezones];
        }
    }
}

// Initialize the clock when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new DigitalClock();
});