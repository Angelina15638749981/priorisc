import os
import sys
import unittest
import subprocess
import hashlib
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './trains')))

try:
    os.mkdir('test/out')
except:
    pass

from pic_gentor.data_generator import FakeTextDataGenerator
from pic_gentor import back_gentor
from pic_gentor.string_gentor import (
    create_strings_from_file,
    create_strings_from_dict,
    create_strings_from_wikipedia,
    create_strings_randomly
)

def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        hash_md5.update(f.read())
    h = hash_md5.hexdigest()
    return h

def empty_directory(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))

# 测试输出
class DataGenerator(unittest.TestCase):
    def test_create_string_from_wikipedia(self):

        strings = create_strings_from_wikipedia(20, 2, 'en')

        self.assertTrue(
            len(strings) == 2 and
            strings[0] != strings[1] and
            len(strings[0].split(' ')) >= 20 and
            len(strings[1].split(' ')) >= 20
        )

    def test_create_string_from_file(self):
        strings = create_strings_from_file('test/test.txt', 6)

        self.assertTrue(
            len(strings) == 6 and
            strings[0] != strings[1] and
            strings[0] == strings[3]
        )

    def test_create_strings_from_dict(self):
        strings = create_strings_from_dict(3, False, 2, ['TEST\n', 'TEST\n', 'TEST\n', 'TEST\n'])

        self.assertTrue(
            len(strings) == 2 and
            len(strings[0].split(' ')) == 3
        )

    def test_generate_data_with_format(self):
        FakeTextDataGenerator.generate(
            0,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_0.jpg') == md5('test/expected_results/TEST TEST TEST_0.jpg')
        )

        os.remove('test/out/TEST TEST TEST_0.jpg')

    def test_generate_data_with_extension(self):
        FakeTextDataGenerator.generate(
            1,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            32,
            'png',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_1.png') == md5('test/expected_results/TEST TEST TEST_1.png')
        )

        os.remove('test/out/TEST TEST TEST_1.png')

    def test_generate_data_with_skew_angle(self):
        FakeTextDataGenerator.generate(
            2,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            15,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_2.jpg') == md5('test/expected_results/TEST TEST TEST_2.jpg')
        )

        os.remove('test/out/TEST TEST TEST_2.jpg')

    def test_generate_data_with_blur(self):
        FakeTextDataGenerator.generate(
            3,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            3,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_3.jpg') == md5('test/expected_results/TEST TEST TEST_3.jpg')
        )

        os.remove('test/out/TEST TEST TEST_3.jpg')

    def test_generate_data_with_sine_distorsion(self):
        FakeTextDataGenerator.generate(
            4,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            3,
            False,
            1,
            1,
            2,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_4.jpg') == md5('test/expected_results/TEST TEST TEST_4.jpg')
        )

        os.remove('test/out/TEST TEST TEST_4.jpg')

    def test_generate_data_with_cosine_distorsion(self):
        FakeTextDataGenerator.generate(
            5,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            3,
            False,
            1,
            2,
            2,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_5.jpg') == md5('test/expected_results/TEST TEST TEST_5.jpg')
        )

        os.remove('test/out/TEST TEST TEST_5.jpg')

    def test_generate_data_with_left_alignment(self):
        FakeTextDataGenerator.generate(
            6,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            600,
            0,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_6.jpg') == md5('test/expected_results/TEST TEST TEST_6.jpg')
        )

        os.remove('test/out/TEST TEST TEST_6.jpg')

    def test_generate_data_with_center_alignment(self):
        FakeTextDataGenerator.generate(
            7,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            800,
            1,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_7.jpg') == md5('test/expected_results/TEST TEST TEST_7.jpg')
        )

        os.remove('test/out/TEST TEST TEST_7.jpg')

    def test_generate_data_with_right_alignment(self):
        FakeTextDataGenerator.generate(
            8,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            1000,
            2,
            '#010101',
            0,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_8.jpg') == md5('test/expected_results/TEST TEST TEST_8.jpg')
        )

        os.remove('test/out/TEST TEST TEST_8.jpg')

    def test_raise_if_handwritten_and_vertical(self):
        try:
            FakeTextDataGenerator.generate(
                9,
                'TEST TEST TEST',
                'test/font.ttf',
                'test/out/',
                64,
                'jpg',
                0,
                False,
                0,
                False,
                1,
                0,
                0,
                True,
                0,
                1000,
                2,
                '#010101',
                1,
                1,
                (5,5,5,5),
                0
            )
            raise Exception("Vertical handwritten did not throw")
        except ValueError:
            pass

    def test_generate_vertical_text(self):
        FakeTextDataGenerator.generate(
            10,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            32,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            1,
            1,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_10.jpg') == md5('test/expected_results/TEST TEST TEST_10.jpg')
        )

        os.remove('test/out/TEST TEST TEST_10.jpg')

    def test_generate_horizontal_text_with_variable_space(self):
        FakeTextDataGenerator.generate(
            11,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            32,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            4,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_11.jpg') == md5('test/expected_results/TEST TEST TEST_11.jpg')
        )

        os.remove('test/out/TEST TEST TEST_11.jpg')

    def test_generate_vertical_text_with_variable_space(self):
        FakeTextDataGenerator.generate(
            12,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            32,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            1,
            2,
            (5,5,5,5),
            0
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_12.jpg') == md5('test/expected_results/TEST TEST TEST_12.jpg')
        )

        os.remove('test/out/TEST TEST TEST_12.jpg')

    def test_generate_text_with_unknown_orientation(self):
        try:
            FakeTextDataGenerator.generate(
                12,
                'TEST TEST TEST',
                'test/font.ttf',
                'test/out/',
                32,
                'jpg',
                0,
                False,
                0,
                False,
                1,
                0,
                0,
                False,
                0,
                -1,
                0,
                '#010101',
                100,
                2,
                (5,5,5,5),
                0
            )
            raise Exception("Unknown orientation did not throw")
        except ValueError:
            pass

    def test_generate_data_with_fit(self):
        FakeTextDataGenerator.generate(
            13,
            'TEST TEST TEST',
            'test/font.ttf',
            'test/out/',
            64,
            'jpg',
            0,
            False,
            0,
            False,
            1,
            0,
            0,
            False,
            0,
            -1,
            0,
            '#010101',
            0,
            1,
            (0,0,0,0),
            1
        )

        self.assertTrue(
            md5('test/out/TEST TEST TEST_13.jpg') == md5('test/expected_results/TEST TEST TEST_13.jpg')
        )

        os.remove('test/out/TEST TEST TEST_13.jpg')

    def test_generate_string_with_letters(self):
        s = create_strings_randomly(1, False, 1, True, False, False, 'en')[0]

        self.assertTrue(
            all([l in string.ascii_letters for l in s])
        )

    def test_generate_string_with_numbers(self):
        s = create_strings_randomly(1, False, 1, False, True, False, 'en')[0]

        self.assertTrue(
            all([l in '0123456789' for l in s])
        )

    def test_generate_string_with_symbols(self):
        s = create_strings_randomly(1, False, 1, False, False, True, 'en')[0]
        
        self.assertTrue(
            all([l in '!"#$%&\'()*+,-./:;?@[\\]^_`{|}~' for l in s])
        )

    def test_generate_chinese_string(self):
        s = create_strings_randomly(1, False, 1, True, False, False, 'cn')[0]
        
        cn_chars = [chr(i) for i in range(19968, 40908)]

        self.assertTrue(
            all([l in cn_chars for l in s])
        )

    def test_generate_data_with_white_background(self):
        back_gentor.plain_white(64, 128).convert('RGB').save('test/out/white_background.jpg')

        self.assertTrue(
            md5('test/out/white_background.jpg') == md5('test/expected_results/white_background.jpg')
        )

        os.remove('tests/out/white_background.jpg')

    def test_generate_data_with_gaussian_background(self):
        back_gentor.gaussian_noise(64, 128).convert('RGB').save('test/out/gaussian_background.jpg')

        self.assertTrue(
            md5('test/out/gaussian_background.jpg') == md5('test/expected_results/gaussian_background.jpg')
        )

        os.remove('test/out/gaussian_background.jpg')

    def test_generate_data_with_quasicrystal_background(self):
        bkgd = back_gentor.quasicrystal(64, 128)
        
        self.assertTrue(
            len(bkgd.histogram()) > 20 and bkgd.size == (128, 64)
        )

class CommandLineInterface(unittest.TestCase):
    def test_output_dir(self):
        args = ['python3', 'run.py', '-c', '1', '--output_dir', '../test/out_2/']
        subprocess.Popen(args, cwd="/").wait()
        self.assertTrue(len(os.listdir('test/out_2/')) == 1)
        empty_directory('test/out_2/')

    def test_language_english(self):
        args = ['python3', 'run.py', '-l', 'en', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('tests/out/')) == 1)
        empty_directory('tests/out/')

    def test_language_french(self):
        args = ['python3', 'run.py', '-l', 'fr', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 1)
        empty_directory('test/out/')

    def test_language_spanish(self):
        args = ['python3', 'run.py', '-l', 'es', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 1)
        empty_directory('test/out/')

    def test_language_german(self):
        args = ['python3', 'run.py', '-l', 'de', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 1)
        empty_directory('test/out/')

    def test_language_chinese(self):
        args = ['python3', 'run.py', '-l', 'cn', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 1)
        empty_directory('test/out/')

    def test_count_parameter(self):
        args = ['python3', 'run.py', '-c', '10', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 10)
        empty_directory('test/out/')

    def test_random_sequences_letter_only(self):
        args = ['python3', 'run.py', '-rs', '-let', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(all([c in string.ascii_letters for f in os.listdir('test/out/') for c in f.split('_')[0]]))
        empty_directory('test/out/')

    def test_random_sequences_number_only(self):
        args = ['python3', 'run.py', '-rs', '-num', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(all([c in '0123456789' for f in os.listdir('test/out/') for c in f.split('_')[0]]))
        empty_directory('test/out/')

    def test_random_sequences_symbols_only(self):
        args = ['python3', 'run.py', '-rs', '-sym', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        with open('test/out/labels.txt', 'r') as f:
            self.assertTrue(all([c in "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~" for c in f.readline().split(' ')[1][:-1]]))
        empty_directory('test/out/')

    def test_handwritten(self):
        args = ['python3', 'run.py', '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 1)
        empty_directory('test/out/')

    def test_personalfont(self):
        args = ['python3', 'run.py', '--font', 'fonts/latin/Aller_Bd.ttf' , '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 1)
        empty_directory('test/out/')

    def test_personalfont_unlocated(self):
        args = ['python3', 'run.py', '--font', 'fonts/latin/unlocatedFont.ttf' , '-c', '1', '--output_dir', '../test/out/']
        subprocess.Popen(args, cwd="trains/").wait()
        self.assertTrue(len(os.listdir('test/out/')) == 0)
        empty_directory('test/out/')

#    def test_word_count(self):
#        args = ['python3', 'run.py', '-c', '1', '-w', '5']
#        subprocess.Popen(args, cwd="trains/").wait()
#        self.assertTrue(False)
#        empty_directory('test/out/')
#
#    def test_extension_jpg(self):
#        args = ['python3', 'run.py', '-c', '1', '-e', 'jpg']
#        subprocess.Popen(args, cwd="trains/").wait()
#        self.assertTrue(False)
#        empty_directory('test/out/')
#
#    def test_extension_png(self):
#        args = ['python3', 'run.py', '-c', '1', '-e', 'png']
#        subprocess.Popen(args, cwd="trains/").wait()
#        self.assertTrue(False)
#        empty_directory('test/out/')
#
#    def test_name_format_0(self):
#        args = ['python3', 'run.py', '-c', '1', '-na', '0']
#        subprocess.Popen(args, cwd="trains/").wait()
#        self.assertTrue(False)
#        empty_directory('test/out/')
#
#    def test_name_format_1(self):
#        args = ['python3', 'run.py', '-c', '1', '-na', '1']
#        subprocess.Popen(args, cwd="trains/").wait()
#        self.assertTrue(False)
#        empty_directory('test/out/')
#
#    def test_name_format_2(self):
#        args = ['python3', 'run.py', '-c', '1', '-na', '2']
#        subprocess.Popen(args, cwd="trains/").wait()
#        self.assertTrue(False)
#        empty_directory('test/out/')

if __name__=='__main__':
    unittest.main()
