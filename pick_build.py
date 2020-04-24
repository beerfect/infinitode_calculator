
import damage

###########################
#     ASSIST FUNCTIONS
###########################

def sort_monsters_by_damage(a, d):
    return [key for (key, value) in sorted(d.items(), key=lambda t: t[1])]
    # return [key for (key, value) in sorted(d.items(), key=lambda t: t[1])][::-1]

def get_least_damaging_monsters(a,d):
    if (len(a)) == 0:
        print('There is no monsters!')
        return []  
    result = []    
    m = d[a[0]]
    for e in a:
        if d[e] == m:
            result.append(e)
    return result


def reduce_effective_towers(effective_towers, least_damaging_monsters):
    top_towers = []
    damage_by_monsters = 0
    # print(f'Reduce_effective_towers()')
    # print(f'{effective_towers=}')
    # print(f'{least_damaging_monsters=}')
    for tower in effective_towers:
        tower_damage = 0
        # print('\n')
        # print(f'Checking {tower=}')
        for monster in least_damaging_monsters:
            # print(f'{tower=}, {monster=} dmg =', damage.from_to[tower][monster])
            tower_damage += damage.from_to[tower][monster]
            # print(f'{tower_damage=}')
            # print(f'Top {damage_by_monsters=}')
            if tower_damage > damage_by_monsters:
                damage_by_monsters = tower_damage
                top_towers = [tower]
            elif damage_by_monsters == tower_damage and tower not in top_towers:
                top_towers.append(tower)
            # print(f'{top_towers=}')
    return top_towers
        
            
























###########################
#      MAIN FUNCTION
###########################

def pick_up_the_composition_of_the_towers(number_of_towers, possible_monsters, locked_towers):
    print('\n')
    print(f'Pick {number_of_towers} towers')
    print(f'Vs monsters: {possible_monsters}')
    print(f'Locked towers: {locked_towers}')
    
    # print('*'*20)
    
    # переменная для результата
    result = []
    
    # переменная для текущего урона
    current_damage = {monster: 0 for monster in possible_monsters}
    # current_damage['regular'] = 0
    # current_damage['jet'] = 2
    # current_damage['fighter'] = 10
    # print(f'{current_damage=}')
    
    # пока не подобрано необходимое число башен:
    while len(result) < number_of_towers:
        # print('_'*20)
        
        sorted_by_damage_monsters = sort_monsters_by_damage(possible_monsters, current_damage)
        # print(f'{sorted_by_damage_monsters=}')
        
        # эффективные башни = все возможные башни
        effective_towers = [tower for tower in damage.from_to if tower not in locked_towers]        
        # print(f'{effective_towers=}')
        
        # пока эффективны несколько башен:
        stopper = 0
        while len(effective_towers) > 1:
        # while len(effective_towers) > 1 and stopper <= 5:
            
            # найти монстра/монстров получающих меньше всех урона
            least_damaging_monsters = get_least_damaging_monsters(sorted_by_damage_monsters, current_damage)
                  
            # print(f'{least_damaging_monsters=}')
            
            #  удалить его/их из текущего списка мобов
            sorted_by_damage_monsters = list(set(sorted_by_damage_monsters) - set(least_damaging_monsters))
            # print(f'{sorted_by_damage_monsters=}')
            
            # найти башню/башни наиболее эффективные против монстра/монстров получающих меньше всех урона
            # сократить список эффективных башен
            effective_towers = reduce_effective_towers(effective_towers,least_damaging_monsters)
            # print(f'Теперь {effective_towers=}')
            
            # если эффективна одна башня:
            if len(effective_towers) == 1:
                # добавить эту башню к ответу
                result.append(effective_towers[0])
                
                # изменить значения входящего урона по монстрам
                for monster in current_damage:
                    current_damage[monster] += damage.from_to[effective_towers[-1]][monster]
            
            # если это последние мобы с минимальным по ним уроном
            elif len(sorted_by_damage_monsters) == 0:
                
                # добавляем первую попавшуюся башню, тк нет разницы 
                result.append(effective_towers[0])
                
                # изменить значения входящего урона по монстрам
                for monster in current_damage:
                    current_damage[monster] += damage.from_to[effective_towers[0]][monster]
                
            
            # stopper +=1
            
        # result.append('f')
    
    d = {}
    for elem in result:
        d[elem] = result.count(elem)
        
    print('\n')
    print('RESULT TOWERS:')
    for tower in d:
        print(f'{tower}: {d[tower]}')
    
    print('\n')
    print('RESULT DMG:')
    for monster in current_damage:
        print(f'{monster} get {current_damage[monster]} dmg')
    
    return result



        


























###########################
#      REALIZATION
###########################

number_of_towers = 66
possible_monsters = ['regular', 'heli', 'armored', 'toxic', 'icy', 'fighter', 'boss', 'strong']
# locked_towers = ['missile', 'flamethrower', 'laser', 'tesla', 'antiair']
# locked_towers = ['missile', 'flamethrower', 'laser', 'tesla', 'antiair', 'multishot']
locked_towers = ['freezing', 'antiair']
# locked_towers = []

pick_up_the_composition_of_the_towers(number_of_towers, possible_monsters, locked_towers)