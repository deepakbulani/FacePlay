# FacePlay

Face recognition is the process of identifying people through facial images, has numerous
practical applications in the area of bio-metrics, information security, access control, law
enforcement, smart cards and surveillance system.We aim to augment the utility of face
recognition with emotion as well as gender detection for the full purview of our project.
Emotion detection and computing aims to enable machines to recognize and synthesize
human emotions. As we all know, a change of user’s emotion is one of the founda-
tion of communication. Emotional states can motivate human’s actions, and can also
supplement the meaning of communication. Thus,in this project we first went through
OpenCV library which is aimed at real time computer vision and includes more than 2500
optimized algorithms,which includes a comprehensive set of both classic and state of the
art computer vision and machine learning algorithms. OpenCV helped us to detect faces
and various facial regions like eyes,nose,lips and jaw and dlib was an improvement over
OpenCV. We have used dlib library for mapping exact facial characteristics to obtain
a higher accuracy during training and testing. Here, Dlib is a modern C++ toolkit
containing machine learning algorithms and tools for creating complex software to solve
real world problems. For gender and emotion detection we make use of FisherFace
Recognizer included under OpenCV which we train using dataset from KDEF(Karolinska
Directed Emotional Faces) and IMDB-WIKI.FisherFace uses Linear Discriminant Analysis
(LDA) to determine the vector representation. It produces float value in the prediction.
This also means that the result is better compared to Eigenface, that is considered first
successful method of face recognition.
