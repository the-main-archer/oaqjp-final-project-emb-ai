from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted by this", "disgust"),
            ("I am so happy I am doing this", "joy"),
            ("I am terrified of the outcome", "fear"),
            ("This makes me so sad", "sadness")
        ]
        
        # Iterate over each test case
        for statement, expected_emotion in test_cases:
            with self.subTest(statement=statement):
                # Call the emotion_detector function
                result = emotion_detector(statement)
                
                # Assert that the returned dominant emotion matches the expected emotion
                self.assertEqual(result['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()