# -*- coding:utf-8 -*-

import editdistance
from constants import Constants, PublishSimilarity
from record import Achievement, Journal, Patent, Proceeding, Thesis

class_type_dict = {
    Achievement: Constants.PUBLICATION_ACHIEVEMENT,
    Journal: Constants.PUBLICATION_JOURNAL,
    Patent: Constants.PUBLICATION_PATENT,
    Proceeding: Constants.PUBLICATION_PROCEEDING,
    Thesis: Constants.PUBLICATION_THESIS,
}

similarity_threshold = 0.9


def set_similarity_threshold(threshold):
    global similarity_threshold
    similarity_threshold = threshold


def get_similarity_threshold():
    global similarity_threshold
    return similarity_threshold


def normalized_edit_distance(str1, str2):
    return 1 - (float(editdistance.eval(str1, str2)) / max(len(str1), len(str2)))


def similar_author(authors1, authors2):
    global similarity_threshold

    def contain_similar_author(author, author_list):
        for author_candidate in author_list:
            if normalized_edit_distance(author, author_candidate) >= similarity_threshold:
                return True
        return False

    bound = min(len(authors1), len(authors2)) * 0.6
    similar_author_count = 0
    for author1 in authors1:
        if not contain_similar_author(author1, authors2):
            continue
        similar_author_count += 1
        if similar_author_count >= bound:
            return True
    return False


def similar_publish(publish1, publish2, category):
    global similarity_threshold
    if type(publish1) != type(publish2):
        return PublishSimilarity.DIFFERENT
    try:
        title1 = getattr(publish1, 'title')
        title2 = getattr(publish2, 'title')
        authors1 = getattr(publish1, 'authors')
        authors2 = getattr(publish2, 'authors')
    except AttributeError:
        return PublishSimilarity.DIFFERENT
    title_similarity = normalized_edit_distance(title1, title2)
    if title_similarity < similarity_threshold:
        return PublishSimilarity.DIFFERENT
    author_similar = similar_author(authors1, authors2)
    if not author_similar:
        return PublishSimilarity.DIFFERENT
    if title_similarity >= 1:
        return PublishSimilarity.SAME
    return PublishSimilarity.SIMILAR


def remove_duplicate(category_dict):
    for category, publish_list in category_dict.items():
        length = len(publish_list)
        duplicate_publish_list = list()
        similar_pair_list = list()
        for i, publish1 in enumerate(publish_list):
            for j in xrange(i + 1, length):
                publish2 = publish_list[j]
                similarity = similar_publish(publish1, publish2, category)
                if similarity == PublishSimilarity.SAME:
                    duplicate_publish_list.append(publish2)
                elif similarity == PublishSimilarity.SIMILAR:
                    similar_pair_list.append((publish1, publish2))
                    # treat similar publish as same
                    duplicate_publish_list.append(publish2)
        for duplicate_publish in duplicate_publish_list:
            try:
                publish_list.remove(duplicate_publish)
            except ValueError:
                continue
    return category_dict


def build_output_str(category_dict, type_order):
    content = ''
    publish_count = 0
    for publish_type in type_order:
        if publish_type not in category_dict:
            continue
        publish_list = category_dict[publish_type]
        content += u'共有%s篇%s:\r\n' % (len(publish_list), Constants.ARTICLE_CLASS_DESC.get(publish_type))
        for publish in publish_list:
            publish_count += 1
            content += u'%s. %s\r\n\r\n' % (publish_count, publish.export())
    return content


def build_output(publish_list):
    publish_type_list = [
        Constants.PUBLICATION_JOURNAL,
        Constants.PUBLICATION_THESIS,
        Constants.PUBLICATION_PROCEEDING,
        Constants.PUBLICATION_ACHIEVEMENT,
        Constants.PUBLICATION_PATENT
    ]
    category_dict = dict()
    for publish in publish_list:
        category = class_type_dict.get(type(publish))
        if category is None:
            continue
        category_dict.setdefault(category, []).append(publish)
    category_dict = remove_duplicate(category_dict)
    return build_output_str(category_dict, publish_type_list)

