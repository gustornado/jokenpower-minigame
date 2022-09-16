import csv
import os.path
from datetime import datetime
from core.config.types import ParticipantType
from core.aux.attack import Attack

class Save:
    def __init__(self):
        self.cache = []
        self.cache_size = 10
        self.filename = 'attacks_pattern.csv'
        self.fieldnames = ['timestamp', 'time_since_start', 'player_type', 'attack_type', 'damage', 'is_counter_attack']
        self.file_exists = os.path.isfile(self.filename)
    
    

    def add_to_cache(self, participant: ParticipantType, attack: Attack, damage:int, now: int):
        self._write_to_file_if_cache_full()
        incoming_row = self._format_to_save(participant, attack, damage, now)
        self.cache.append(incoming_row)
    
    def save_remanescent_cache(self,):
        self._write_to_file_if_cache_full(True)

        
    def _write_to_file_if_cache_full(self, ignore_overflow: bool=False):
        if self._check_cache_overload() or ignore_overflow:
            self._write_to_csv()
            self.cache.clear()
    

    def _format_to_save(self, participant: ParticipantType, attack: Attack, damage: int, time_since_start: int) -> dict:
        return {
            'timestamp'         : datetime.now(),
            'time_since_start'  : time_since_start,
            'player_type'       : participant.value,
            'attack_type'       : attack.type.value,
            'damage'            : damage,
            'is_counter_attack' : attack.is_reaction
        }
    
    def _check_cache_overload(self):
        return len(self.cache) >= self.cache_size
        

    def _write_to_csv(self):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)

            if not self.file_exists:
                writer.writeheader()
                self.file_exists = True
            for row in self.cache:
                writer.writerow(row)