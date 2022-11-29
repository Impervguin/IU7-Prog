import TextFuncs as tf


class TextProcessor:
    def __init__(self, text: list):
        self.text = text
        self.alignment = None

    def __str__(self):
        return "\n".join(self.text)

    def __aling_to_left(self):
        for ind, line in enumerate(self.text):
            was_gap = False
            new_line = ""
            for symb in line.strip():
                if symb == " " and not was_gap:
                    was_gap = True
                elif symb == " ":
                    continue
                else:
                    was_gap = False
                new_line += symb
            self.text[ind] = new_line

    def __align_to_right(self):
        max_len = 0
        for ind, line in enumerate(self.text):
            was_gap = False
            new_line = ""
            for symb in line.strip():
                if symb == " " and not was_gap:
                    was_gap = True
                elif symb == " ":
                    continue
                else:
                    was_gap = False
                new_line += symb
            max_len = max(max_len, len(new_line))
            self.text[ind] = new_line
        for ind, line in enumerate(self.text):
            self.text[ind] = " " * (max_len - len(line)) + line

    def __align_to_width(self):
        max_len = 0
        for ind, line in enumerate(self.text):
            was_gap = False
            new_line = ""
            for symb in line.strip():
                if symb == " " and not was_gap:
                    was_gap = True
                elif symb == " ":
                    continue
                else:
                    was_gap = False
                new_line += symb
            max_len = max(max_len, len(new_line))
            self.text[ind] = new_line
        for ind, line in enumerate(self.text):
            n_gaps = line.count(" ")
            gap_width, n_gap_replace = divmod(max_len - len(line) + n_gaps, n_gaps)
            self.text[ind] = self.text[ind].replace(" ", " " * gap_width).replace(" " * gap_width,
                                                                                  " " * (gap_width + 1),
                                                                                  n_gap_replace)

    def __delete_empty_lines(self):
        for ind, line in enumerate(self.text):
            if line.strip() == "":
                del self.text[ind]

    def align(self, alignment="self"):
        if alignment == "self":
            if self.alignment is not None:
                self.align(self.alignment)
        elif alignment == "left":
            self.alignment = "left"
            self.__aling_to_left()
        elif alignment == "right":
            self.alignment = "right"
            self.__align_to_right()
        elif alignment == "width":
            self.alignment = "width"
            self.__align_to_width()

    def delete_word(self, word):
        for ind_l, line in enumerate(self.text):
            line_split = line.split()
            for ind_w, w in enumerate(line_split):
                if tf.get_word_without_punction(w) == word:
                    punc = tf.get_punction_without_word(w)
                    if ind_w != 0:
                        line_split[ind_w - 1] = line_split[ind_w - 1] + punc
                        del line_split[ind_w]
                    elif ind_l != 0:
                        self.text[ind_l - 1] = self.text[ind_l - 1] + punc
                        del line_split[ind_w]
                    else:
                        line_split[ind_w] = punc
            self.text[ind_l] = " ".join(line_split)
        self.align()

    def replace_word(self, word, rep):
        for ind_l, line in enumerate(self.text):
            line_split = line.split()
            for ind_w, w in enumerate(line_split):
                if tf.get_word_without_punction(w) == word:
                    punc = tf.get_punction_without_word(w)
                    line_split[ind_w] = rep + punc
            self.text[ind_l] = " ".join(line_split)
        self.align()

    def do_calcs(self):
        for ind_l, line in enumerate(self.text):
            line_split = line.split()
            i = 1
            while i < len(line_split) - 1:
                if line_split[i] in ("*", "/"):
                    try:
                        num1 = float(line_split[i - 1])
                        num2 = float(line_split[i + 1])
                        res = f"{num1 * num2 if line_split[i] == '*' else num1 / num2:.5g}"
                        line_split[i + 1] = res
                        del line_split[i - 1:i + 1]
                        i -= 1
                    except BaseException:
                        pass
                i += 1
            self.text[ind_l] = " ".join(line_split)
        self.align()

    def pop_sentence(self):
        now_sentence = [(0, 0), 0]
        max_sentence = ((0, 0), (0, 0), 0)
        for ind_l, line in enumerate(self.text):
            now_word_cons = 0
            for ind_s, symb in enumerate(line):
                if symb == " ":
                    now_sentence[1] = max(now_sentence[1], now_word_cons)
                    now_word_cons = 0
                elif symb.upper() in tf.CONSORNANTS:
                    now_word_cons += 1
                elif symb in tf.END_SENTENCE_SYMB:
                    now_sentence[1] = max(now_sentence[1], now_word_cons)
                    if now_sentence[1] > max_sentence[2]:
                        max_sentence = (now_sentence[0], (ind_l, ind_s), now_sentence[1])
                    now_sentence = [(ind_l, ind_s + 1), 0]

        st_l = max_sentence[0][0]
        ed_l = max_sentence[1][0]
        self.text = self.text[:st_l + 1] + self.text[ed_l:]
        self.text[st_l] = self.text[st_l][:max_sentence[0][1]]
        self.text[st_l + 1] = self.text[st_l + 1][max_sentence[1][1] + 1:]
        self.__delete_empty_lines()
        self.align()


if __name__ == "__main__":
    test = ["   Неделю спустя Дориан, Грей сидел lllllllllll в оранжерее",
            "     своей, усадьбы СелбиРойял,   беседуя с  40 / 20.   хорошенькой герцогиней Монмаут,",
            "    которая гостила у него вместе     с мужем, высохшим шестидесятилетним стариком."
            ]
    tp = TextProcessor(test)
    tp.align("width")
    print(tp)
    tp.delete_word("Дориан")
    print(tp)
