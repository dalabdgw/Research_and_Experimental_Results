import pygame.midi
def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number%12]

def number_to_note_octave(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    octave = (number // 12) + 1
    note = notes[number % 12]
    return note, octave
def readInput(input_device):
    n = 0
    current_key = ''
    while True:
        if input_device.poll():
            event = input_device.read(1)[0]
            data = event[0]
            timestamp = event[1]
            note_number = data[1]
            velocity = data[2]

            if velocity > 0 and n % 5 == 0:
                print(f'note number: {note_number}')
                print(f'current note: {number_to_note(note_number)}')
                print(f'current velocity: {velocity}')
                print(f'current octave: {number_to_note_octave(note_number)}')
                print('-----------------------------------')
            n += 1

#            time.sleep(1)

if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(0) #only in my case the id is 2
    readInput(my_input)