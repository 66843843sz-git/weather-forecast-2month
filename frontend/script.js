const API_BASE = 'http://localhost:5000/api';
let forecastData = [];

document.addEventListener('DOMContentLoaded', function() {
    loadData();
    setupEventListeners();
});

function setupEventListeners() {
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            switchTab(this.dataset.tab);
        });
    });

    const slider = document.getElementById('daySlider');
    if (slider) {
        slider.addEventListener('input', function() {
            updateForecastDisplay(parseInt(this.value));
        });
    }
}

async function loadData() {
    try {
        const response = await fetch(`${API_BASE}/forecast`);
        const data = await response.json();
        forecastData = data.data || [];

        document.getElementById('loading').style.display = 'none';
        document.getElementById('tabs').style.display = 'flex';

        renderForecast(15);
    } catch (error) {
        console.error('Error loading data:', error);
        showError('加载数据失败，请检查API服务');
    }
}

function showError(message) {
    const loading = document.getElementById('loading');
    loading.innerHTML = `<div style="color: #e53935; font-size: 1.2em;">❌ ${message}</div>`;
}

function switchTab(tabName) {
    document.querySelectorAll('.tab-pane').forEach(pane => {
        pane.classList.remove('active');
    });

    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    document.getElementById(tabName).classList.add('active');
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
}

function updateForecastDisplay(days) {
    document.getElementById('dayDisplay').textContent = `显示: 前${days}天`;
    renderForecast(days);
}

function renderForecast(days) {
    const grid = document.getElementById('forecastGrid');
    if (!grid) return;
    
    grid.innerHTML = '';

    forecastData.slice(0, days).forEach(day => {
        const card = document.createElement('div');
        card.className = 'forecast-card';

        const weatherEmoji = getWeatherEmoji(day.weather_type);

        card.innerHTML = `
            <div class="forecast-date">${day.date}</div>
            <div style="text-align: center; font-size: 2em;">${weatherEmoji}</div>
            <div style="text-align: center; font-weight: 600; margin: 10px 0;">${day.weather_type}</div>
            <div class="forecast-temp">
                <span style="color: #e53935;">高: ${day.temperature.high}°C</span>
                <span style="color: #64b5f6;">低: ${day.temperature.low}°C</span>
            </div>
            <div style="font-size: 0.85em; color: #666; margin-top: 10px;">
                <div>💧 湿度: ${day.humidity}%</div>
                <div>🌧️ 降雨: ${day.rainfall}mm</div>
                <div>💨 风速: ${day.wind_speed}m/s</div>
            </div>
            <div style="text-align: center; font-size: 0.8em; color: #999; margin-top: 10px;">
                可信度: ${day.confidence.toFixed(0)}%
            </div>
        `;

        grid.appendChild(card);
    });
}

function getWeatherEmoji(type) {
    const emojiMap = {
        '晴': '☀️',
        '多云': '⛅',
        '阴': '☁️',
        '雨': '🌧️',
        '暴雨': '⛈️'
    };
    return emojiMap[type] || '🌤️';
}
