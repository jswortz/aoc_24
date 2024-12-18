import asyncio
from typing import List

TEST_DATA = "2333133121414131402"


with open("d_09/challenge09.data", "r") as file:
    challenge09_data = file.read()


def read_disk_map(disk_map: str) -> List[int]:
    char_disk_map = [*disk_map]
    filename = 0
    output = []
    for i, char in enumerate(char_disk_map):
        instruction = int(char)
        if i % 2 == 0:
            file_string = [filename] * instruction
            output.extend(file_string)
            filename += 1
        else:
            file_string = [-1] * instruction
            output.extend(file_string)
    return output


def compress_disk(disk: List[int]) -> List[int]:
    while not check_if_line_compressed(disk):
        last_non_empty = find_last_nonempty(disk)
        first_empty = find_first_empty(disk)
        disk[first_empty] = disk[last_non_empty]
        disk[last_non_empty] = -1

    return disk


def compress_disk_blocks(disk: List[int]) -> List[int]:
    ids = get_ids(disk)
    for id in reversed([id for id in ids if id != 0]):  # find the last one first
        indices = [i for i, x in enumerate(disk) if x == id]
        block_length = len(indices)
        first_avail_block = check_for_first_block(
            disk=disk, block_len=block_length, block_start=indices[0]
        )
        if first_avail_block > -1:
            for i, b in zip(
                indices, range(first_avail_block, first_avail_block + block_length)
            ):
                disk[i] = -1
                disk[b] = id
    return disk


def get_ids(disk: List[int]) -> List[int]:
    ids = list(set(disk))
    return [id for id in ids if id != -1]


def check_for_first_block(disk: List[int], block_len: int, block_start: int) -> int:
    for i, id in enumerate(disk):
        if i > block_start:
            break
        if id == -1:
            try:
                if disk[i : i + block_len] == [-1] * block_len:
                    return i
            except IndexError as e:
                print("Error :", e)
    return -1


def check_if_line_compressed(line: List[int]) -> bool:
    return find_last_nonempty(line) < find_first_empty(line)


def find_last_nonempty(line: List[int]) -> int:
    for i, char in reversed(list(enumerate(line))):
        if char != -1:
            return i


def find_first_empty(line: List[int]) -> int:
    for i, char in enumerate(line):
        if char == -1:
            return i


def get_checksum(line: List[int]):
    checksum = 0
    for i, char in enumerate(line):
        if char != -1:
            checksum += i * int(char)
    return checksum


async def main(data: str):
    disk = read_disk_map(disk_map=data)
    print("Uncompressed disk: \n", disk)
    compressed_disk = compress_disk(disk=disk)
    print("Compressed disk: \n", compressed_disk)
    print("Checksum: ", get_checksum(compressed_disk))
    compressed_disk2 = compress_disk_blocks(disk=disk)
    print("Compressed disk: \n", compressed_disk2)
    print("Checksum: ", get_checksum(compressed_disk2))


if __name__ == "__main__":
    asyncio.run(main(data=TEST_DATA))
    asyncio.run(main(data=challenge09_data))
