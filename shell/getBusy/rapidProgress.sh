#!/bin/bash

workingDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

action=$($workingDir/rand.sh $workingDir/actions)
object=$($workingDir/rand.sh $workingDir/objects)
echo $action $object
sleep 1
echo -ne '|----------|----------|----------|----------| (0%)\r'
sleep 0.05
echo -ne '|----------|----------|----------|----------| (1%)\r'
sleep 0.05
echo -ne '|----------|----------|----------|----------| (2%)\r'
sleep 0.05
echo -ne '|#---------|----------|----------|----------| (3%)\r'
sleep 0.05
echo -ne '|#---------|----------|----------|----------| (4%)\r'
sleep 0.05
echo -ne '|##--------|----------|----------|----------| (5%)\r'
sleep 0.05
echo -ne '|##--------|----------|----------|----------| (6%)\r'
sleep 0.05
echo -ne '|##--------|----------|----------|----------| (7%)\r'
sleep 0.05
echo -ne '|###-------|----------|----------|----------| (8%)\r'
sleep 0.05
echo -ne '|###-------|----------|----------|----------| (9%)\r'
sleep 0.05
echo -ne '|####------|----------|----------|----------| (10%)\r'
sleep 0.05
echo -ne '|####------|----------|----------|----------| (11%)\r'
sleep 0.05
echo -ne '|####------|----------|----------|----------| (12%)\r'
sleep 0.05
echo -ne '|#####-----|----------|----------|----------| (13%)\r'
sleep 0.05
echo -ne '|#####-----|----------|----------|----------| (14%)\r'
sleep 0.05
echo -ne '|######----|----------|----------|----------| (15%)\r'
sleep 0.05
echo -ne '|######----|----------|----------|----------| (16%)\r'
sleep 0.05
echo -ne '|######----|----------|----------|----------| (17%)\r'
sleep 0.05
echo -ne '|#######---|----------|----------|----------| (18%)\r'
sleep 0.05
echo -ne '|#######---|----------|----------|----------| (19%)\r'
sleep 0.05
echo -ne '|########--|----------|----------|----------| (20%)\r'
sleep 0.05
echo -ne '|########--|----------|----------|----------| (21%)\r'
sleep 0.05
echo -ne '|########--|----------|----------|----------| (22%)\r'
sleep 0.05
echo -ne '|#########-|----------|----------|----------| (23%)\r'
sleep 0.05
echo -ne '|#########-|----------|----------|----------| (24%)\r'
sleep 0.05
echo -ne '|##########|----------|----------|----------| (25%)\r'
sleep 0.05
echo -ne '|##########|----------|----------|----------| (26%)\r'
sleep 0.05
echo -ne '|##########|----------|----------|----------| (27%)\r'
sleep 0.05
echo -ne '|##########|#---------|----------|----------| (28%)\r'
sleep 0.05
echo -ne '|##########|#---------|----------|----------| (29%)\r'
sleep 0.05
echo -ne '|##########|##--------|----------|----------| (30%)\r'
sleep 0.05
echo -ne '|##########|##--------|----------|----------| (31%)\r'
sleep 0.05
echo -ne '|##########|##--------|----------|----------| (32%)\r'
sleep 0.05
echo -ne '|##########|###-------|----------|----------| (33%)\r'
sleep 0.05
echo -ne '|##########|###-------|----------|----------| (34%)\r'
sleep 0.05
echo -ne '|##########|####------|----------|----------| (35%)\r'
sleep 0.05
echo -ne '|##########|####------|----------|----------| (36%)\r'
sleep 0.05
echo -ne '|##########|####------|----------|----------| (37%)\r'
sleep 0.05
echo -ne '|##########|#####-----|----------|----------| (38%)\r'
sleep 0.05
echo -ne '|##########|#####-----|----------|----------| (39%)\r'
sleep 0.05
echo -ne '|##########|######----|----------|----------| (40%)\r'
sleep 0.05
echo -ne '|##########|######----|----------|----------| (41%)\r'
sleep 0.05
echo -ne '|##########|######----|----------|----------| (42%)\r'
sleep 0.05
echo -ne '|##########|#######---|----------|----------| (43%)\r'
sleep 0.05
echo -ne '|##########|#######---|----------|----------| (44%)\r'
sleep 0.05
echo -ne '|##########|########--|----------|----------| (45%)\r'
sleep 0.05
echo -ne '|##########|########--|----------|----------| (46%)\r'
sleep 0.05
echo -ne '|##########|########--|----------|----------| (47%)\r'
sleep 0.05
echo -ne '|##########|#########-|----------|----------| (48%)\r'
sleep 0.05
echo -ne '|##########|#########-|----------|----------| (49%)\r'
sleep 0.05
echo -ne '|##########|##########|----------|----------| (50%)\r'
sleep 0.05
echo -ne '|##########|##########|----------|----------| (51%)\r'
sleep 0.05
echo -ne '|##########|##########|----------|----------| (52%)\r'
sleep 0.05
echo -ne '|##########|##########|#---------|----------| (53%)\r'
sleep 0.05
echo -ne '|##########|##########|#---------|----------| (54%)\r'
sleep 0.05
echo -ne '|##########|##########|##--------|----------| (55%)\r'
sleep 0.05
echo -ne '|##########|##########|##--------|----------| (56%)\r'
sleep 0.05
echo -ne '|##########|##########|##--------|----------| (57%)\r'
sleep 0.05
echo -ne '|##########|##########|###-------|----------| (58%)\r'
sleep 0.05
echo -ne '|##########|##########|###-------|----------| (59%)\r'
sleep 0.05
echo -ne '|##########|##########|####------|----------| (60%)\r'
sleep 0.05
echo -ne '|##########|##########|####------|----------| (61%)\r'
sleep 0.05
echo -ne '|##########|##########|####------|----------| (62%)\r'
sleep 0.05
echo -ne '|##########|##########|#####-----|----------| (63%)\r'
sleep 0.05
echo -ne '|##########|##########|#####-----|----------| (64%)\r'
sleep 0.05
echo -ne '|##########|##########|######----|----------| (65%)\r'
sleep 0.05
echo -ne '|##########|##########|######----|----------| (66%)\r'
sleep 0.05
echo -ne '|##########|##########|######----|----------| (67%)\r'
sleep 0.05
echo -ne '|##########|##########|#######---|----------| (68%)\r'
sleep 0.05
echo -ne '|##########|##########|#######---|----------| (69%)\r'
sleep 0.05
echo -ne '|##########|##########|########--|----------| (70%)\r'
sleep 0.05
echo -ne '|##########|##########|########--|----------| (71%)\r'
sleep 0.05
echo -ne '|##########|##########|########--|----------| (72%)\r'
sleep 0.05
echo -ne '|##########|##########|#########-|----------| (73%)\r'
sleep 0.05
echo -ne '|##########|##########|#########-|----------| (74%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|----------| (75%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|----------| (76%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|----------| (77%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#---------| (78%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#---------| (79%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|##--------| (80%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|##--------| (81%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|##--------| (82%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|###-------| (83%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|###-------| (84%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|####------| (85%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|####------| (86%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|####------| (87%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#####-----| (88%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#####-----| (89%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|######----| (90%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|######----| (91%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|######----| (92%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#######---| (93%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#######---| (94%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|########--| (95%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|########--| (96%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|########--| (97%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#########-| (98%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|#########-| (99%)\r'
sleep 0.05
echo -ne '|##########|##########|##########|##########| (100%)\r'
sleep 0.05
echo 
echo "Done!"
sleep 2
