from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_emotion_detection(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        emo1 = result1["dominant_emotion"]
        self.assertEqual(emo1, "joy")
        
        result2 = emotion_detector("I am really mad about this")
        emo2 = result2["dominant_emotion"]
        self.assertEqual(emo2, "anger")
        
        result3 = emotion_detector("I feel disgusted just hearing about this")
        emo3 = result3["dominant_emotion"]
        self.assertEqual(emo3, "disgust")
        
        result4 = emotion_detector("I am so sad about this")
        emo4 = result4["dominant_emotion"]
        self.assertEqual(emo4, "sadness")
        
        result5 = emotion_detector("I am really afraid that this will happen")
        emo5 = result5["dominant_emotion"]
        self.assertEqual(emo5, "fear")

unittest.main()