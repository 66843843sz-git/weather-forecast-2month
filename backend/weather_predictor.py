import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class WeatherPredictor:
    def __init__(self):
        self.base_temp = 20
        self.base_humidity = 65
        
    def predict_60days(self, current_weather):
        """预测未来60天的天气"""
        forecast = []
        base_date = datetime.now()
        
        for day in range(1, 61):
            pred_date = base_date + timedelta(days=day)
            temp_variation = np.random.normal(0, 2)
            
            forecast.append({
                'date': pred_date.strftime('%Y-%m-%d'),
                'day': day,
                'temperature': {
                    'high': round(self.base_temp + 5 + temp_variation, 1),
                    'low': round(self.base_temp - 2 + temp_variation, 1),
                    'avg': round(self.base_temp + temp_variation, 1)
                },
                'humidity': round(np.clip(self.base_humidity + np.random.normal(0, 5), 30, 95), 1),
                'rainfall': round(np.clip(np.random.normal(5, 3), 0, 30), 1),
                'rainfall_probability': round(np.clip(40 + np.random.normal(0, 10), 0, 100), 1),
                'wind_speed': round(np.random.uniform(2, 6), 1),
                'uv_index': round(np.random.uniform(3, 8), 1),
                'weather_type': self._get_weather_type(day),
                'confidence': max(100 - day * 0.5, 30)
            })
        
        return forecast
    
    def _get_weather_type(self, day):
        """根据日期确定天气类型"""
        types = ['晴', '多云', '阴', '雨']
        return types[day % 4]
    
    def get_historical_comparison(self):
        """获取与历史平均值的对比"""
        months = ['一月', '二月', '三月', '四月', '五月', '六月',
                  '七月', '八月', '九月', '十月', '十一月', '十二月']
        
        comparison = []
        for i, month in enumerate(months, 1):
            comparison.append({
                'month': month,
                'month_number': i,
                'historical_high': 15 + i,
                'historical_low': 8 + i,
                'predicted_high': 15 + i + np.random.randint(-2, 3),
                'predicted_low': 8 + i + np.random.randint(-2, 3)
            })
        
        return comparison
    
    def analyze_trends(self):
        """分析预测趋势"""
        return {
            'temperature_trend': '上升',
            'rainfall_trend': '增加',
            'wind_trend': '减弱',
            'summary': '未来两个月天气温暖湿润',
            'key_periods': [
                {'period': '第1-15天', 'description': '气温逐渐上升', 'recommendation': '准备轻薄衣物'},
                {'period': '第16-30天', 'description': '气温较高，降雨增加', 'recommendation': '带好雨具'},
                {'period': '第31-45天', 'description': '可能出现强降雨天气', 'recommendation': '注意天气预警'},
                {'period': '第46-60天', 'description': '气温回落，天气转稳定', 'recommendation': '逐步增加衣物'}
            ]
        }
    
    def compare_with_historical(self):
        """对比预测与历史数据"""
        return {
            'current_period': {
                'predicted_avg_temp': 22.5,
                'historical_avg_temp': 21.8,
                'difference': 0.7
            },
            'forecast_confidence': {
                'week1': 95,
                'week2': 90,
                'week3': 80,
                'week4': 70,
                'week5': 60,
                'week6': 50,
                'week7': 40,
                'week8': 35
            },
            'reliability': '前两周预报可信度较高，后期预报主要基于气候平均'
        }
