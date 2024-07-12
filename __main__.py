from openai4vision import openai4vision

if __name__ ==  '__main__':
    image_url = "https://digitalcontent.api.tesco.com/v2/media/ghs/500d66f6-89d8-4c9d-9c24-5668caa57312/075056a7-8414-408e-a0d5-1e56caeeaad2.jpeg?h=960&w=960"
    openai4vision.tag_image(image_url)