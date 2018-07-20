def get_image(self, top_data):
    # imagesがあればthumbnail をkeyとして追加する
    for a in top_data['hits']:
        if a.get('images'):
            d = {'thumbnail':{
                'credit': a['images'][0]['credit'],
                'format': a['images'][0]['format'],
                'height': a['images'][0]['height'],
                'image_id': a['images'][0]['image_id'],
                'revision': a['images'][0]['revision'],
                'src_image_url': a['images'][0]['src_image_url'],
                'width': a['images'][0]['width']
                }}
    top_data['hits'].insert(0, d)
    # test
    self.top_data = top_data
