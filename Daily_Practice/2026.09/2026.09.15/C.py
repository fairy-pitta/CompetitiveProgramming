N, M = map(int, input().split())
students = []
checkpoints = []

for _ in range(N):
    a, b = map(int, input().split())
    students.append([a,b])

for _ in range(M):
    c, d = map(int, input().split())
    checkpoints.append([c,d])

for student in students:

    student_x = student[0]
    student_y = student[1]
    nearest_checkpoint = 10**18
    nearest_distance = 10**18

    for checkpoint_num in range(M):
        checkpoint_x = checkpoints[checkpoint_num][0]
        checkpoint_y = checkpoints[checkpoint_num][1]
        distance = abs(student_x-checkpoint_x) + abs(student_y-checkpoint_y)

        if distance < nearest_distance:
            nearest_distance = distance 
            nearest_checkpoint = checkpoint_num + 1 # 0-indexed
        elif distance == nearest_distance:
            nearest_checkpint = min(checkpoint_num+1, nearest_checkpoint)
        
    print(nearest_checkpoint)
        