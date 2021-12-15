# Собрал Django REST framework & vue в одном проекте
'''
-Создал директорию
-создал и активировал виртуалку
-в settings зарегал приложение и rest...., дописал MEDIA
-написал модели
-сделал миграции
-создал суперпользователя
-зарегал модели в админке
-в api: написал serializers, views
-заполнил главный urls, и urls приложения
-в админке создал посты
-проверил, как выводятся в json
-- создал frontend
vue create .

Настраиваем:
? Generate project in current directory? (Y/n)  Y

выбираем (enter)
	Manually select features

		дальше ПРОБЕЛом подтверждаем
		 ◉ Choose Vue version
 		◉ Babel
 		◯ TypeScript
 		◯ Progressive Web App (PWA) Support
 		◉ Router
		❯◉ Vuex
 		◯ CSS Pre-processors
 		◉ Linter / Formatter   +ENTER
 		◯ Unit Testing
 		◯ E2E Testing

			❯ 3.x   +ENTER 
				? Use history mode for router? (Requires proper server setup for 					index fallback in production) (Y/n) Y
					>ESLint + Standard config
						❯◉ Lint on save
							❯ In dedicated config files  
								? Save this as a preset for future projects? 								 (y/N) N
(ждем окончания установки)

запускаю сервер
npm run serve
в components создаем (или переименовываем фаил) BlogPostList.vue
чистим его, остается
<template>
	<div class="post-list">
		<h1>Good afternoon</h1> 
	</div>
</template>

<script>
export default {
	name: 'BlogPostList',
	props: {
		posts: Array
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
	margin: 40px 0 0;
}
ul {
	list-style-type: none;
	padding: 0;
}
li {
	display: inline-block;
	margin: 0 10px;
}
a {
	color: #42b983;
}
</style>


настраиваем Home.vue
<template>
	<div class="home">
		<img alt="Vue logo" src="../assets/logo.png">
		<BlogPostList :posts='posts'/> # это передаю пропсы posts='posts'
	</div>
</template>

<script>
// @ is an alias to /src
import BlogPostList from '@/components/BlogPostList' #импортировали

export default {
	name: 'Home',
	components: {
		BlogPostList #зарегистрировали
	},
	data () {
		return { #здесь будут наши посты
		posts: []
		}
	},
	methods: {
		async getBlogPost () {
	
		}
	}
}
</script>

останавливаем сервак, устанавливаем библиотеку axios (аналог requests, отправляем через нее запросы. Находимся в дир-рии frontend)
CTRL + C
npm install axios -s   #nout package manager

Запускаем сервак, проверяем, что бы станица выводилась

пишем в Home
<template>
	<div class="home">
		<img alt="Vue logo" src="../assets/logo.png">
		<BlogPostList :posts='posts'/>
	</div>
</template>

<script>
// @ is an alias to /src
import BlogPostList from '@/components/BlogPostList'
import axios from 'axios'

export default {
	name: 'Home',
	components: {
		BlogPostList
	},
	data () {
		return {
			posts: []
		}
	},
	methods: {
		async getBlogPost () {
			try {
				const response = await axios.get('http://127.0.0.1:8000/api/') # скопировал со страницы, где выводятся все мои посты Blog Post List Api (backend в json)

				console.log(response.data)
			} catch (e) {
				console.log('error!')
			}
		}
	}
}
</script>



устанавливаем django-cors-headers 3.10.1 (в терминале backend !!!)
(https://pypi.org/project/django-cors-headers/)
	открываем терминал backend, тормозим его, устанавливаем библиотеку
pip install django-cors-headers

дописываем в 
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'blog_app',
	'rest_framework',
	"corsheaders"
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	"corsheaders.middleware.CorsMiddleware",
	"django.middleware.common.CommonMiddleware",
]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
	'http://127.0.0.1:8080', #это backend
	'http://localhost:8080'  #это frontend
]


в Home обозначаю ВебХук (промежуточные элементы, которые срабатывают в первую очередь)
<template>
	<div class="home">
		<BlogPostList :posts='posts'/>
	</div>
</template>

<script>
// @ is an alias to /src
import BlogPostList from '@/components/BlogPostList.vue'
import axios from 'axios'

export default {
	name: 'Home',
	components: {
		BlogPostList
	},
	data () {
		return {
			posts: []
		}
	},
	methods: {
		async getBlogPost () {
			try {
				const response = await axios.get('http://127.0.0.1:8000/api/')
				console.log(response.data)
			} catch (e) {
				console.log('error!')
			}
		}
	},
	mounted () {
		this.getBlogPost()
	}
}
</script>



запускаю сервер backend
 ./manage.py runserver

проверяю, что выводятся посты в консоль


в Home заполняю модель посты, кладу в нее данные
this.posts = response.data это мы обращаемся к  posts: [], кладем в нее данные из запроса	 и дальше передаем в компоненту <BlogPostList :posts='posts'/>
			
<template>
	<div class="home">
		<BlogPostList :posts='posts'/>
	</div>
</template>

<script>
// @ is an alias to /src
import BlogPostList from '@/components/BlogPostList.vue'
import axios from 'axios'

export default {
	name: 'Home',
	components: {
		BlogPostList
	},
	data () {
		return {
			posts: []
		}
	},
methods: {
	async getBlogPost () {
		try {
			const response = await axios.get('http://127.0.0.1:8000/api/')
			// console.log(response.data)
			this.posts = response.data
		} catch (e) {
			console.log('error!')
		}
	}
},
  mounted () {
	this.getBlogPost()
  }
}
</script>


в BlogPostList.vue
в BlogPostList.vue мы уже принимаем некий posts: Array м рсиаеися его разложить
<template>
	<div class="post-list">
		<h1>Good afternoon</h1>
		<div class="post" v-for="post in posts" :key="post.id">
			<h3>{{ post.title }}</h3>
			<img :src="post.img" alt="">
			<div class="post-date">
				{{ post.updated_at}}
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'BlogPostList',
	props: {
			posts: Array
		}
	}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	.post {
		background-color: grey;
		bottom: 2px solid black;
		padding: 20px;
		margin: 20px;
	}
</style>
'''
