player = {
  'name': 'nico',
  'age': 12,
  'alive': True,
  'fav_food':["🍕", "🍔"]
}
# 요소 접근
# 변수명.get("키명")
print(player.get('age'))
print(player.get('fav_food'))

print(player)

# 요소 제거
player.pop('age')
print(player)

# 요소 추가
player['xp'] = 1500
print(player)

player['fav_food'].append("🍜")
print(player)