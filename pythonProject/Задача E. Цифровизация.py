def check_passports(num_boxes, boxes):
    results = []

    for box in boxes:
        ids = set()  # Отслеживаем уникальные идентификационные номера коров в ящике
        children = {}  # Отслеживаем отношения родитель-потомок

        for passport in box:
            cow_id, father_id, mother_id = passport
            if cow_id in ids or (father_id == cow_id and mother_id == cow_id):
                results.append("INCORRECT")
                break  # Прекращаем проверку этого ящика, если обнаружено нарушение
            else:
                ids.add(cow_id)

                if father_id in children:
                    if children[father_id] != mother_id:
                        results.append("INCORRECT")
                        break
                else:
                    children[father_id] = mother_id

        else:  # Этот блок будет выполнен, если нарушений не обнаружено
            results.append("CORRECT")

    return results


def main():
    num_boxes = int(input())
    boxes = []
    for _ in range(num_boxes):
        num_passports = int(input())
        passports = [list(map(int, input().split())) for _ in range(num_passports)]
        boxes.append(passports)

    results = check_passports(num_boxes, boxes)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()