#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    routes = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            destination = input("Пункт назначения? ")
            number = input("Номер поезда? ")
            time = input("Время отправления?(формат чч:мм) ")

            route = {
                'destination': destination,
                'number': number,
                'time': time
            }

            routes.append(route)
            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 4,
                '-' * 20
            )
            print(line)
            print(
                '| {:^30} | {:^4} | {:^20} |'.format(
                    "Пункт назначения",
                    "№",
                    "Время"
                )
            )
            print(line)

            for route in routes:
                print(
                    '| {:<30} | {:>4} | {:<20} |'.format(
                        route.get('destination', ''),
                        route.get('number', ''),
                        route.get('time', '')
                    )
                )
            print(line)

        elif command == 'select':
            time2 = input("Выберите время отправления(формат чч:мм): ")
            time3 = int(time2.replace(':', ''))
            count = 0

            for route in routes:
                time1 = route.get('time')
                time1 = int(time1.replace(':', ''))
                if time1 > time3:
                    count += 1
                    print(
                        '{:>4} {} {}'.format("№" + route.get('number'),
                                             route.get('destination', ''),
                                             route.get('time'))
                    )

            if count == 0:
                print("Такие маршруты не найдены")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select - нати маршруты по времени")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
