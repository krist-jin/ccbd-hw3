#!/usr/bin/python

import cPickle as pickle
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import sys
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize

sys.stderr.write("Started mapper.\n");
TIME_DELIMETER = "#######"

def word_feats(words):
    return dict([(word, True) for word in words])


def subj(subjLine):
    subjgen = subjLine.lower()
    # Replace term1 with your subject term
    subj1 = "god"
    if subjgen.find(subj1) != -1:
        subject = subj1
        return subject
    else:
        subject = "No match"
        return subject


def main(argv):
    # classifier = pickle.load(open("classifier.p", "rb"))
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
    negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'negative') for f in negids]
    posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'positive') for f in posids]
    trainfeats = posfeats+negfeats
    classifier = NaiveBayesClassifier.train(trainfeats)
    for line in sys.stdin:
        try:
            time_stamp = line.rstrip().rsplit(TIME_DELIMETER, 1)[-1]
            tolk_posset = word_tokenize(line.rstrip())
            d = word_feats(tolk_posset)
            subjectFull = subj(line)
            if subjectFull == "No match":
                print "LongValueSum:" + " " + subjectFull + ": " + "\t" + "1"
            else:
                # print "LongValueSum:" + " " + subjectFull + ": " + classifier.classify(d) + "\t" + "1"
                print "LongValueSum:" + " " + subjectFull + ": " + time_stamp + ": " + classifier.classify(d) + "\t" + "1"
        except Exception, e:
            continue


if __name__ == "__main__":
    main(sys.argv)