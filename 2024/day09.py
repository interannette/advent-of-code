from collections import Counter
import logging
from typing import Iterable

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class Day09Puzzle:
    file_sizes = list[int]
    block_sizes = list[int]
    total_file_size = int

    def __init__(self, s: str):
        file_sizes = []
        block_sizes = []
        for i in s:
            if len(file_sizes) == len(block_sizes):
                file_sizes.append(int(i))
            else:
                block_sizes.append(int(i))
        self.file_sizes = file_sizes
        self.block_sizes = block_sizes
        self.total_file_size = sum([f for f in file_sizes])

        logger.debug(f"{len(file_sizes)} files. total size {self.total_file_size}")

    def star1(self) -> int:
        compacted = []
        file_count = len(self.file_sizes)
        remaining_files = [
            i for i in range(len(self.file_sizes)) if self.file_sizes[i] > 0
        ]
        remaining_blocks = [
            i for i in range(len(self.block_sizes)) if self.block_sizes[i] > 0
        ]

        while len(compacted) < self.total_file_size:
            file_id = min(remaining_files)
            file_size = self.file_sizes[file_id]
            if file_size > 0:
                for l in range(file_size):
                    compacted.append(file_id)
                    self.file_sizes[file_id] = self.file_sizes[file_id] - 1
                remaining_files.remove(file_id)
            else:
                break

            if not remaining_files or not remaining_blocks:
                break

            block_id = file_id
            block_size = self.block_sizes[file_id]

            if block_size > 0:
                for i in range(block_size):
                    file_id = max(remaining_files)
                    file_size = self.file_sizes[file_id]
                    if file_size > 0:
                        compacted.append(file_id)
                        self.file_sizes[file_id] = self.file_sizes[file_id] - 1
                        if self.file_sizes[file_id] == 0:
                            remaining_files.remove(file_id)
                            if not remaining_files:
                                break
                remaining_blocks.remove(block_id)

        frequency = Counter(compacted)
        logger.debug(f"{len(frequency)} ids. {frequency.total()}")
        return sum([i * compacted[i] for i in range(len(compacted))])

    def star2(self) -> int:

        file_start_end: list[tuple[int, int]] = []
        block_start_end: list[tuple[int, int]] = []
        current = 0
        for i in range(len(self.file_sizes)):
            file_start_end.append((current, current + self.file_sizes[i] - 1))
            current = current + self.file_sizes[i]
            if i < len(self.block_sizes) and self.block_sizes[i] > 0:
                block_start_end.append((current, current + self.block_sizes[i] - 1))
                current = current + self.block_sizes[i]

        logger.debug(f"files: {file_start_end}")
        logger.debug(f"blocks: {block_start_end}")
        # attempt to move each file exactly once in order of decreasing file ID number
        # starting with the file with the highest file ID number.
        # If there is no span of free space to the left of a file that is large enough to fit the file,
        # the file does not move.

        for file_id in range(len(self.file_sizes) - 1, -1, -1):
            file_size = self.file_sizes[file_id]
            print(f"checking {file_id} with size {file_size}")
            # find the earliest block that fits file_size

            smallest_block_id = -1
            for b in range(len(block_start_end)):
                if (block_start_end[b][1] - block_start_end[b][0]) >= file_size:
                    smallest_block_id = b
                    break

            # if you can find a place to move:
            if smallest_block_id > -1:
                logger.debug(f"moving file {file_id} to block {smallest_block_id}")
                # put file_id in block_id
                file_start_end[file_id] = (
                    block_start_end[smallest_block_id][0],
                    block_start_end[smallest_block_id][0] + file_size - 1,
                )

                # update block_start_end;
                # if full use of block
                if block_start_end[smallest_block_id][1] == file_start_end[file_id][1]:
                    block_start_end[smallest_block_id] = (-1, -1)
                else:
                    # if partial use of block
                    block_start_end[smallest_block_id] = (
                        file_start_end[file_id][1] + 1,
                        block_start_end[smallest_block_id][1],
                    )
            # else can't move this file, continue
            else:
                logger.debug(f"not able to move file {file_id}")

        logger.debug(f"files: {file_start_end}")
        logger.debug(f"blocks: {block_start_end}")

        checksum = 0
        for file_id in range(len(file_start_end)):
            checksum += file_id * (
                file_start_end[file_id][1] - file_start_end[file_id][0]
            )

        return checksum


test_input = True
if test_input:
    input = """2333133121414131402"""
else:
    input = open("inputs/day09.txt").readlines().pop()

puzzle = Day09Puzzle(input)
print(puzzle.star2())

# 6520497170536 too high
# 37356198108968
