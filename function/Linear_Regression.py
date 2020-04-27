import tensorflow as  tf 
# tensorflow 프레임워크 선언후, 지도학습을 위한 데이터 셋 정의
X = 
Y = 

# H의 초기값은 무작위(random_normal)로 지정, [0]-스칼라, [1]-벡터, [2]-집합
# 값이 계속해서 갱신(변수)되므로, Variable(객체라 첫글자 대문자)
w = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

# 제곱 - tf.square()
# 모두 더해서 평균 - tf.reduce_mean()
hypothesis = W * X + b 
cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf. train.GradientDescentOptimizer(learning_rate=0.01)  # 미분 이후 과정
train = optimizer.minimize(cost)               #  r = 0.01   
sess = tf.Session()
sess.run(tf.global_variables_initializer())  # Variable이 객체라 초기화를 해야 활성화
for step in range(2001):  # 2001번 학습, 200번째마다 cost, w, b출력  
    sess.run(train)
    if step % 200 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))