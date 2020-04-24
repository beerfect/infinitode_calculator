import damage

def calgulate_build_dps(towers, monsters):
    result = {monster: 0 for monster in monsters}
    for tower in towers:
        for monster in result:
            result[monster] += damage.from_to[tower][monster] * towers[tower]    
    
    # beauty console report
    print()
    print('Calculating dps...')
    print(f'{towers=}')
    print(f'{monsters=}')
    print()
    for monster in result:
        print(f'{monster} get {result[monster]} dps')
    
    return result
    
###########################
#      REALIZATION
###########################

monsters = ['regular', 'heli', 'armored', 'toxic', 'icy', 'fighter', 'boss', 'strong']

towers = {
    'splash': 17,
    'sniper': 17,
    'minigun': 15,
    'tesla': 17,
}

calgulate_build_dps(towers, monsters)
