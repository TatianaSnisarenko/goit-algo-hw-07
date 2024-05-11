

class Comment:
    def __init__(self, text, author, answers=[]):
        self.text = text
        self.author = author
        self.answers = answers
        self.is_deleted = False
        self.height = 1

    def add_reply(self, reply):
        self.answers.append(reply)
        reply.height = max([reply.height, self.height + 1])

    def remove_reply(self):
        self.text = 'Цей коментар було видалено.'
        self.is_deleted = True

    def get_height(comment):
        if not comment:
            return 0
        return comment.height

    def __str__(self, seen=set()):
        if self in seen:
            return ""
        seen.add(self)
        author = '' if self.is_deleted else self.author + ": "
        ret = "\t" * (self.height - 1) + author + str(self.text) + "\n"
        for answer in self.answers:
            ret += answer.__str__(seen)
        return (ret)

    def display(self):
        print(self.__str__())


if __name__ == '__main__':
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")
    reply3 = Comment("Яка книга?", "Сергій")

    root_comment.add_reply(reply1)

    reply1_1 = Comment(
        "Не книжка, а перевели купу паперу ні нащо...", "Сергій")

    reply1.add_reply(reply1_1)
    reply1_2 = Comment("Ти її прочитав?", "Андрій")
    reply1_1.add_reply(reply1_2)

    root_comment.add_reply(reply2)
    root_comment.add_reply(reply3)

    reply1.remove_reply()

    root_comment.display()
