from pymental.meta import Model, SKIP
from pymental.fields import GenericField, RelatedField, ListField


def test_generic_field():
    xml = '<root foo="bar"><hello>world</hello></root>'

    class F(Model):
        _tag = 'root'
        hello = GenericField('hello')
        a = GenericField(tag='a', default='Missing')
        b = GenericField(tag='b', description='Without default')

    f = F.parse(xml)

    assert f.hello == 'world'
    assert f._attributes['foo'] == 'bar'
    assert isinstance(f._fields['hello'], GenericField)
    assert f.a == 'Missing'
    assert f.b is SKIP


def test_related_field():
    xml = '''<root>
                <hello>
                    <world>foo</world>
                </hello>
            </root>'''

    class Hello(Model):
        _tag = 'hello'
        world = GenericField('world')

    class F(Model):
        _tag = 'root'
        hello = RelatedField('hello', Hello)

    f = F.parse(xml)

    assert f.hello.world == 'foo'
    assert isinstance(f.hello, Hello)


def test_list_field():
    xml = '''<root>
                <hello>
                    <world>foo</world>
                </hello>
                <hello>
                    <world>bar</world>
                </hello>
            </root>'''

    class Hello(Model):
        _tag = 'world'
        world = GenericField('world')

    class F(Model):
        _tag = 'root'
        hello = ListField('hello', Hello)

    f = F.parse(xml)

    assert f.hello[0].world == 'foo'
    assert isinstance(f.hello, list)


def test_unparse():
    xml = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<root foo="bar"><hello><world>foo</world></hello>'
           '<hello><world>bar</world></hello></root>')

    class Hello(Model):
        _tag = 'world'
        world = GenericField('world')

    class F(Model):
        _tag = 'root'
        hello = ListField('hello', Hello)

    f = F.parse(xml)
    unparsed = f.unparse(pretty=False)

    assert xml == unparsed
