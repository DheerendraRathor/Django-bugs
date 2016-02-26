from prefetch_one.models import *
from django.core import management
management.call_command('flush', verbosity=0, interactive=False)

u1 = User.objects.create(username='a', password='a')
u2 = User.objects.create(username='b', password='b')
u3 = User.objects.create(username='c', password='c')
u4 = User.objects.create(username='d', password='d')

g1 = Group.objects.create()
g2 = Group.objects.create()
g3 = Group.objects.create()

c1 = Concept.objects.create(group=g1)
c2 = Concept.objects.create(group=g1)
c3 = Concept.objects.create(group=g1)
c4 = Concept.objects.create(group=g1)
c5 = Concept.objects.create(group=g1)


c6 = Concept.objects.create(group=g2)
c7 = Concept.objects.create(group=g2)
c8 = Concept.objects.create(group=g2)

v1 = Video.objects.create()
v2 = Video.objects.create()
v3 = Video.objects.create()
v4 = Video.objects.create()
v5 = Video.objects.create()

c1.videos.add(v1, v2, v3, v4)
c2.videos.add(v2, v3, v4, v5)
c3.videos.add(v2, v5)


q1 = Quiz.objects.create()
q2 = Quiz.objects.create()
q3 = Quiz.objects.create()
q4 = Quiz.objects.create()


qh1 = QuizHistory.objects.create(quiz=q1, user=u1)
qh2 = QuizHistory.objects.create(quiz=q1, user=u2)
qh3 = QuizHistory.objects.create(quiz=q1, user=u3)
qh4 = QuizHistory.objects.create(quiz=q1, user=u4)


qh5 = QuizHistory.objects.create(quiz=q2, user=u1)
qh6 = QuizHistory.objects.create(quiz=q2, user=u2)
qh7 = QuizHistory.objects.create(quiz=q2, user=u3)
qh8 = QuizHistory.objects.create(quiz=q2, user=u4)


qh9 = QuizHistory.objects.create(quiz=q3, user=u1)
qh10 = QuizHistory.objects.create(quiz=q3, user=u2)
qh11 = QuizHistory.objects.create(quiz=q3, user=u3)
qh12 = QuizHistory.objects.create(quiz=q3, user=u4)


m1 = Marker.objects.create(video=v1)
m2 = Marker.objects.create(video=v1)
m3 = Marker.objects.create(video=v1)
m4 = Marker.objects.create(video=v1)

m5 = Marker.objects.create(video=v2)
m6 = Marker.objects.create(video=v2)
m7 = Marker.objects.create(video=v2)
m8 = Marker.objects.create(video=v2)


qm1 = QuizMarker.objects.create(quiz=q1, video=v1)
qm2 = QuizMarker.objects.create(quiz=q2, video=v1)
qm3 = QuizMarker.objects.create(quiz=q3, video=v1)
qm4 = QuizMarker.objects.create(quiz=q4, video=v1)

qm5 = QuizMarker.objects.create(quiz=q1, video=v1)
qm6 = QuizMarker.objects.create(quiz=q2, video=v2)
qm7 = QuizMarker.objects.create(quiz=q3, video=v2)
qm8 = QuizMarker.objects.create(quiz=q4, video=v2)


groups = Group.objects.filter(id=1).order_by('id').prefetch_related(
    Prefetch(
        'concepts',
        queryset=Concept.objects.order_by('id').prefetch_related(
            Prefetch(
                'videos__markers',
                queryset=QuizMarker.objects.prefetch_related(
                    Prefetch('quiz__quiz_histories',
                             queryset=QuizHistory.objects.filter(user=u1).select_related('quiz'))
                ),
            )
        )
    )
)

groups = list(groups)
