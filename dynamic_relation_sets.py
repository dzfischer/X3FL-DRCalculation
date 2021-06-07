import numpy as np

# yes this data entry is impossible to read, I apologize in advance.
# Easy enough to convert to read from csv or something if you want tho
se = 100
al = 15
fl = 10
fr = 5
ne = 0
ho = -15
en = -30

# 1 for checking stable foelists, 0 for checking stable alliances (+10 vs +8)
calc_foelist = 1

# # to watch how the algo steps thru a specific target list
# unique_check = np.array([1,1,1,1,0,1,1,0,0,1,1,1,1,1,1])
unique_check = np.array([])

# # --------- with Yaki and ATF ver
# faction_list = ['Argon', 'ATF', 'Boron', 'Goner', 'Paranid', 'Pirates', 'Split', 'Teladi',\
#                 'Terran', 'Yaki', 'OTAS', 'Atreus', 'Duke\'s', 'NMMC', 'Strong Arms', 'TerraCorp']
# # factions:   ar, af, bo, go, pa, pi, sp, tl, te, ya, ot, at, du, nm, st, tc
# opinion_ar = [se, en, al, fl, en, en, ho, ne, en, en, al, fr, en, ne, ho, al]
# opinion_af = [en, se, en, ne, en, en, en, ne, al, en, en, ne, en, ne, en, ne]
# opinion_bo = [al, en, se, fr, ho, en, en, ne, en, en, fr, al, en, ne, en, fr]
# opinion_go = [fl, ne, fr, se, ne, ne, ne, ne, ne, ne, ne, ne, ne, ne, ne, al]
# opinion_pa = [en, en, ho, ne, se, en, al, ne, en, en, en, ho, en, ne, fr, en]
# opinion_pi = [en, en, en, en, en, se, ne, ne, en, en, en, en, al, ne, ne, en]
# opinion_sp = [ho, en, en, ne, al, ne, se, ne, en, en, ho, en, en, ne, al, ho]
# opinion_tl = [ne, ne, ne, ne, ne, ne, ne, se, ne, en, ne, ne, ne, al, ne, ne]
# opinion_te = [en, al, en, ne, en, en, en, ne, se, en, en, en, en, ne, en, ne]
# opinion_ya = [en, en, en, ho, en, en, en, en, en, se, en, en, en, ne, ne, en]
# opinion_ot = [al, en, fr, ne, en, en, ho, ne, en, en, se, en, ne, ne, ho, en]
# opinion_at = [fr, en, al, ne, ho, en, en, ne, en, en, en, se, ne, ne, en, fr]
# opinion_du = [en, en, en, en, en, al, en, ne, en, en, ne, ne, se, en, ne, ne]
# opinion_nm = [ne, ne, ne, ne, ne, ne, ne, al, ne, ne, ne, ne, en, se, ne, ne]
# opinion_st = [ho, en, en, en, fr, ne, al, ne, en, ne, ho, en, ne, ne, se, ho]
# opinion_tc = [al, ne, fr, al, en, en, ho, ne, ne, en, en, fr, ne, ne, ho, se]
# opinion_array = np.array([opinion_ar, opinion_af, opinion_bo, opinion_go, opinion_pa, opinion_pi, \
#     opinion_sp, opinion_tl, opinion_te, opinion_ya, opinion_ot, opinion_at, opinion_du, opinion_nm, opinion_st, opinion_tc])

# --------- sans ATF ver
faction_list = ['Argon', 'Boron', 'Goner', 'Paranid', 'Pirates', 'Split', 'Teladi',\
               'Terran', 'Yaki', 'OTAS', 'Atreus', 'Duke\'s', 'NMMC', 'Strong Arms', 'TerraCorp']
# factions:   ar, bo, go, pa, pi, sp, tl, te, ya, ot, at, du, nm, st, tc
opinion_ar = [se, al, fl, en, en, ho, ne, en, en, al, fr, en, ne, ho, al]
opinion_af = [en, en, ne, en, en, en, ne, al, en, en, ne, en, ne, en, ne]
opinion_bo = [al, se, fr, ho, en, en, ne, en, en, fr, al, en, ne, en, fr]
opinion_go = [fl, fr, se, ne, ne, ne, ne, ne, ne, ne, ne, ne, ne, ne, al]
opinion_pa = [en, ho, ne, se, en, al, ne, en, en, en, ho, en, ne, fr, en]
opinion_pi = [en, en, en, en, se, ne, ne, en, en, en, en, al, ne, ne, en]
opinion_sp = [ho, en, ne, al, ne, se, ne, en, en, ho, en, en, ne, al, ho]
opinion_tl = [ne, ne, ne, ne, ne, ne, se, ne, en, ne, ne, ne, al, ne, ne]
opinion_te = [en, en, ne, en, en, en, ne, se, en, en, en, en, ne, en, ne]
opinion_ya = [en, en, ho, en, en, en, en, en, se, en, en, en, ne, ne, en]
opinion_ot = [al, fr, ne, en, en, ho, ne, en, en, se, en, ne, ne, ho, en]
opinion_at = [fr, al, ne, ho, en, en, ne, en, en, en, se, ne, ne, en, fr]
opinion_du = [en, en, en, en, al, en, ne, en, en, ne, ne, se, en, ne, ne]
opinion_nm = [ne, ne, ne, ne, ne, ne, al, ne, ne, ne, ne, en, se, ne, ne]
opinion_st = [ho, en, en, fr, ne, al, ne, en, ne, ho, en, ne, ne, se, ho]
opinion_tc = [al, fr, al, en, en, ho, ne, ne, en, en, fr, ne, ne, ho, se]
opinion_array = np.array([opinion_ar, opinion_bo, opinion_go, opinion_pa, opinion_pi, \
    opinion_sp, opinion_tl, opinion_te, opinion_ya, opinion_ot, opinion_at, opinion_du, opinion_nm, opinion_st, opinion_tc])

# # ------ sans Yaki and ATF
# faction_list = ['Argon', 'Boron', 'Goner', 'Paranid', 'Pirates', 'Split', 'Teladi',\
#                 'Terran', 'OTAS', 'Atreus', 'Duke\'s', 'NMMC', 'Strong Arms', 'TerraCorp']
# # factions:   ar, bo, go, pa, pi, sp, tl, te, ot, at, du, nm, st, tc
# opinion_ar = [se, al, fl, en, en, ho, ne, en, al, fr, en, ne, ho, al]
# opinion_bo = [al, se, fr, ho, en, en, ne, en, fr, al, en, ne, en, fr]
# opinion_go = [fl, fr, se, ne, ne, ne, ne, ne, ne, ne, ne, ne, ne, al]
# opinion_pa = [en, ho, ne, se, en, al, ne, en, en, ho, en, ne, fr, en]
# opinion_pi = [en, en, en, en, se, ne, ne, en, en, en, al, ne, ne, en]
# opinion_sp = [ho, en, ne, al, ne, se, ne, en, ho, en, en, ne, al, ho]
# opinion_tl = [ne, ne, ne, ne, ne, ne, se, ne, ne, ne, ne, al, ne, ne]
# opinion_te = [en, en, ne, en, en, en, ne, se, en, en, en, ne, en, ne]
# opinion_ot = [al, fr, ne, en, en, ho, ne, en, se, en, ne, ne, ho, en]
# opinion_at = [fr, al, ne, ho, en, en, ne, en, en, se, ne, ne, en, fr]
# opinion_du = [en, en, en, en, al, en, ne, en, ne, ne, se, en, ne, ne]
# opinion_nm = [ne, ne, ne, ne, ne, ne, al, ne, ne, ne, en, se, ne, ne]
# opinion_st = [ho, en, en, fr, ne, al, ne, en, ho, en, ne, ne, se, ho]
# opinion_tc = [al, fr, al, en, en, ho, ne, ne, en, fr, ne, ne, ho, se]
# opinion_array = np.array([opinion_ar, opinion_bo, opinion_go, opinion_pa, opinion_pi, \
#     opinion_sp, opinion_tl, opinion_te, opinion_ot, opinion_at, opinion_du, opinion_nm, opinion_st, opinion_tc])

########################

pass_set_list = []
set_extreme_high = [0,[]]
set_extreme_low  = [200,[]]


def opinion_from_missions(mission_list):
    # Given a list of how much notoriety is given to each faction, return net result notoriety with all factions
    opinion_list = []
    for pos, missions in enumerate(mission_list):
        # print(mission_list)
        # print(opinion_array[pos])
        opinion_list.append(np.sum(mission_list * opinion_array[pos]))
    return opinion_list


def check_possible_stable(target_relations):
    # entries of 0 in target_relations are targeted enemies, starting 1 are targeted allies
    # first check if all allies are negative; if so, impossible, return 0
    # then check if all allies positive; if so, done, possible, return 1
    # else, add 1 to mission of ally with most negative opinion, and repeat

    mission_list = target_relations.copy()
    mission_ignores = np.ones(len(faction_list)) - target_relations

    # ~10,000 steps necessary for no timeouts on all sets, 800 good enough that timeouts are for ones that'll end up impossible anyway.
    for _ in range(800):
        # zero out the factions we don't care about
        faction_opinions = opinion_from_missions(mission_list) * target_relations

        if np.array_equal(unique_check, target_relations):
            print(faction_opinions)

        # check if lowest is -2x choice, and already assigned 10 missions; prevents loop w/ no Duke's, but yes NMMC or similar
        if (faction_opinions - mission_ignores < 0).all() or (np.min(faction_opinions) < -2*se and np.max(mission_list) > 10) :
            # print(f'{target_relations} is impossible')
            return -1
        elif (faction_opinions + mission_ignores > 0).all():
            # take a note if most or least efficient just for interest
            notoriety_ratio = 100 * np.sum(faction_opinions) / np.sum(se * mission_list)
            if notoriety_ratio > set_extreme_high[0]:
                set_extreme_high[0] = notoriety_ratio
                set_extreme_high[1] = mission_list
            elif notoriety_ratio < set_extreme_low[0]:
                set_extreme_low[0] = notoriety_ratio
                set_extreme_low[1] = mission_list
            # print('Possible set!')
            # print(mission_list, notoriety_ratio)
            return notoriety_ratio
        else:
            mission_list[np.argmin(faction_opinions + mission_ignores)] += 1

    print('---- Timeout for:')
    print(target_relations)
    print(mission_list)
    print(faction_opinions)
    return -1

def check_if_subset(current_target_list, successful_target_lists):
    # inefficient cycling through successful lists to make sure we're not calculating something that has fewer allies
    # than a set we already know works; e.g. don't check if "A, C" as allies works if we already know "A, B, C" works
    for target_list in successful_target_lists:
        if -1 not in target_list[0] - current_target_list:
            return True
    return False

def check_if_internal_conflict(proposed_ally_list):
    # Check faction of listed proposed allies, if a rival faction is in listed proposed allies
    for faction_num, opinion_list in enumerate(opinion_array):
        if proposed_ally_list[faction_num] == 1:
            for relation_num, opinion in enumerate(opinion_list):
                if opinion < 0 and proposed_ally_list[relation_num] == 1:
                    return False
    return True


# check each possible combination of ally/foe for ~16 factions... o.0
for checknum, selected_foe_numeric in enumerate(reversed(range(2**len(faction_list)))):
    # binary representation of all combinations to get ally/foe list, from all allies (111...1) to all foes (000...0), held as an array
    selected_foes = np.array([int(bin_digit) for bin_digit in f'{selected_foe_numeric:0{len(faction_list)}b}'])
    
    # #####
    # # early truncation for testing
    # if selected_foe_numeric < 2**len(faction_list)-8000:
    #     break

    if checknum%1000 == 0:
        print(f'{checknum}/{2**len(faction_list)} checked...')

    # check each list first if a superset is in pass_set_list, we can ignore these
    if check_if_subset(selected_foes, pass_set_list) == True:
        continue

    if calc_foelist:
        # verify if possible, putting possible ones in pass_set
        notoriety_ratio = check_possible_stable(selected_foes)
        if notoriety_ratio != -1:
            pass_set_list.append([selected_foes, notoriety_ratio])
    else:
        if check_if_internal_conflict(selected_foes):
            pass_set_list.append([selected_foes])

if calc_foelist:
    # printing out a list of all stable foes and the efficiencies for each set
    print(f'BEGINNING READOUT OF FOELIST FROM {len(pass_set_list)} SETS:')
    for num, passes in enumerate(pass_set_list):
        drops = np.ones(len(faction_list)) - passes[0]
        first_entry = True
        for pos, faction_index in enumerate(drops):
            if faction_index == 1:
                if first_entry == True:
                    print(f'{num+1:03}. {passes[1]:04.1f}%: ', end='')
                    first_entry = False
                else:
                    print(' - ', end='')
                print(f'{faction_list[pos]}', end ='')
        if first_entry == True:
            print('Possible to befriend all factions!')
        else:
            print()

    print('Extremes:')
    print(f'Most effective set is {set_extreme_high[0]:.1f}%:')
    print(set_extreme_high[1])
    print(f'Least effective set is {set_extreme_low[0]:.1f}%:')
    print(set_extreme_low[1])
else:
    # printing out a list of all valid alliances
    print('Beginning readout of valid alliances:')
    # print(pass_set_list)
    for num, passes in enumerate(pass_set_list):
        first_entry = True
        for pos, faction_index in enumerate(passes[0]):
            if faction_index == 1:
                if first_entry == True:
                    print(f'{num+1:03}: ', end='')
                    first_entry = False
                else:
                    print(' - ', end='')
                print(f'{faction_list[pos]}', end ='')
        if first_entry == False:
            print()
        else:
            print('Possible to befriend no faction??')