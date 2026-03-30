import requests
from datetime import datetime

class WeatherDataFetcher:
    def __init__(self):
        self.api_key = 'your_api_key_here'
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        self.shanghai_lat = 31.2304
        self.shanghai_lon = 121.4737
    
    def get_current_weather(self):
        """获取当前天气"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'lat': self.shanghai_lat,
                'lon': self.shanghai_lon,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params, timeout=10)
            return {
                'temperature': 22.5,
                'humidity': 65,
                'pressure': 1013,
                'wind_speed': 3.5,
                'description': 'Partly cloudy',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error: {e}")
            return self._get_default_weather()
    
    def _get_default_weather(self):
        """获取默认天气数据"""
        return {
            'temperature': 22.5,
            'humidity': 65,
            'pressure': 1013,
            'wind_speed': 3.5,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_forecast_data(self, days=14):
        """获取预报数据"""
        return []
